""" These methods provide support for publishing or exporting recipes. """
import pathlib
import jinja2
import pdfkit

import gitrecipes.utils as utils

def _load_templates():
    """ Load the Jinja templates used for publishing. """
    env = jinja2.Environment(
        loader=jinja2.PackageLoader(__name__, 'static/templates'),
        autoescape=jinja2.select_autoescape(['html'])
    )
    return env

def publish_print(directory):
    """ Publish all the recipes in this directory as PDFs. """
    pdfdir = pathlib.Path(f"{directory}/pdf/")
    pdfdir.mkdir(parents=True, exist_ok=True)

    recipe_data = utils.load_valid_recipes(directory)
    j2_templates = _load_templates()
    print_template = j2_templates.get_template('print.html')

    for recipe in recipe_data:
        utils.LOGGER.info('Creating a PDF for %s..', recipe["name"])
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

        pdfkit.from_string(rendered_html, f'{pdfdir}/{recipe["filename"]}.pdf', options=options)

def publish_html(directory):
    """
    Publish all the recipes in this directory as html pages with an index page to link them
    all, creating a browsable static website.
    """
    htmldir = pathlib.Path(f"{directory}/html/")
    htmldir.mkdir(parents=True, exist_ok=True)

    j2_templates = _load_templates()
    recipe_template = j2_templates.get_template('recipe.html')
    index_template = j2_templates.get_template('index.html')

    recipe_data = utils.load_valid_recipes(directory)
    recipe_index = []
    # Create a list of all the recipes we're formatting so they can be easily
    # navigated through
    for recipe in recipe_data:
        # Everything we need to template should already be in the yaml file,
        # except the static link
        recipe_filename = f'{recipe["filename"]}.html'
        recipe_index.append({
            'name': recipe['name'],
            'source': recipe['source'],
            'link': recipe_filename
        })

        pathlib.Path(htmldir / recipe_filename).write_text(recipe_template.render(**recipe))

    # Create the index page with links to all the recipes
    pathlib.Path(htmldir / "index.html").write_text(index_template.render(recipes=recipe_index))
