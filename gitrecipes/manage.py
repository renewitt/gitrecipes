""" Functionality used to manage your recipes. """
import yaml
import jinja2
import pathlib
import pdfkit

import gitrecipes.validate

from gitrecipes import LOGGER

def _load_recipes_from_dir(directory):
    """ Return a list of all the file contents in this directory that are valid recipes. """
    recipe_index = pathlib.Path.cwd() / directory
    recipes = []
    for path in recipe_index.glob("*"):
        if path.suffix in ['.yaml', '.yml']:
            contents = yaml.safe_load(path.read_text())
            if contents is None:
                LOGGER.error(f'It looks like {path.name} is an empty file, skipping.')
                continue

            if not gitrecipes.validate.validate_recipe(contents):
                LOGGER.error(f'Unable to properly load file {path.name}, skipping.')
                continue

            recipes.append(contents)

    return recipes

def list_all_recipes(directory):
    """
    List all the recipes that can be loaded and parsed.

    :param directory: The directory to load recipes from
    :returns: Alphabetically sorted list of recipe names
    """
    recipes = _load_recipes_from_dir(directory)
    recipe_names = [recipe['name'] for recipe in recipes]
    return sorted(recipe_names)

def _load_templates():
    """ Load the Jinja templates used for publishing. """
    env = jinja2.Environment(
        loader=jinja2.PackageLoader(__name__, 'static/templates'),
        autoescape=jinja2.select_autoescape(['html'])
    )
    return env

def publish_print(directory):
    """ Publish all the recipes in this directory as PDFs. """
    pdf = pathlib.Path("pdf/")
    pdf.mkdir(parents=True, exist_ok=True)

    recipe_data = _load_recipes_from_dir(directory)
    j2_templates = _load_templates()
    print_template = j2_templates.get_template('print.html')

    # Create a list of all the recipes we're formatting so they can be easily
    # navigated through
    for recipe in recipe_data:
        LOGGER.info(f'Working on creating a PDF for {recipe["name"]}..')
        recipe_filename = f"{recipe['name'].lower().replace(' ', '_')}"
        rendered_html = print_template.render(**recipe)

        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'lowquality': '',
            'quiet': ''
        }

        pdfkit.from_string(rendered_html, f'pdf/{recipe_filename}.pdf', options=options)

def publish_html(directory):
    """
    Publish all the recipes in this directory as html pages with an index page to link them
    all, creating a browsable static website.
    """
    html = pathlib.Path("html/")
    html.mkdir(parents=True, exist_ok=True)

    j2_templates = _load_templates()
    recipe_template = j2_templates.get_template('recipe.html')
    index_template = j2_templates.get_template('index.html')

    recipe_data = _load_recipes_from_dir(directory)
    recipe_index = []
    # Create a list of all the recipes we're formatting so they can be easily
    # navigated through
    for recipe in recipe_data:
        # Everything we need to template should already be in the yaml file,
        # except the static link
        recipe_filename = f"{recipe['name'].lower().replace(' ', '_')}.html"
        recipe_index.append({
            'name': recipe['name'],
            'source': recipe['source'],
            'link': recipe_filename
        })

        pathlib.Path(html / f"{recipe_filename}").write_text(recipe_template.render(**recipe))

    # Create the index page with links to all the recipes
    pathlib.Path(html / f"index.html").write_text(index_template.render(recipes=recipe_index))