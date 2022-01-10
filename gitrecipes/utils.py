""" Helper utilities used by most functionality. """
import logging
import pathlib

import yaml

import gitrecipes.validate

LOGGER = logging.getLogger(__name__)
HANDLER = logging.StreamHandler()
FORMATTER = logging.Formatter('%(message)s')
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)

def load_valid_recipes(directory):
    """
    Return a list of dictionaries, with all valid recipes and their tags from this directory.

    :param directory: Directory path to load recipes from
    :returns: A list of all valid recipes.
    """
    recipe_index = pathlib.Path.cwd() / directory
    recipes = []
    for path in recipe_index.glob("*"):
        # Pathlib gets all files with glob, including hidden ones. Since we're managing this with
        # git and there's likely to be hidden files, we filter these out. We also allow recipes to
        # be ignored if they are prefixed with the !, so filter all of those out too.
        if path.name.startswith('.') or path.name.startswith('!'):
            continue

        if path.suffix not in ['.yaml', '.yml']:
            LOGGER.debug('Skipping non yaml file %s', path)
            continue

        try:
            contents = yaml.safe_load(path.read_text())
        except yaml.parser.ParserError:
            LOGGER.error(
                "There's something wrong with the YAML syntax in the %s file, skipping.",
                path.name)

        if contents is None:
            LOGGER.error('It looks like %s is an empty file, skipping.', path.name)
            continue

        if not gitrecipes.validate.validate_recipe(contents):
            LOGGER.error(
                "Recipe is not formatted as expected or has no content. Unable to process file %s, skipping.",
                path.name)
            continue

        recipes.append(contents)

    return recipes
