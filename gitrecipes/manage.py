""" Functionality used to manage your recipes. """
import collections

import gitrecipes.utils as utils

def list_all_recipes(directory):
    """
    List all the recipes that can be loaded and parsed.

    :param directory: The directory to load recipes from
    :returns: Alphabetically sorted list of recipe names
    """
    recipes = utils.load_valid_recipes(directory)
    # Return the recipe names, source and the tags as a comma separated string for nice display
    recipe_data = []
    for recipe in recipes:
        data = (recipe['name'],  recipe['source'], ', '.join(sorted(recipe['tags'])))
        recipe_data.append(data)
    return sorted(recipe_data)

def search_recipes(directory, search):
    """
    Load all recipes and find all the recipes which have a tag or name which matches the
    supplied search.

    :param directory: The directory to load recipes from
    :param search: The string to match against recipe tags
    :returns: Alphabetically sorted list of recipe names
    """
    search = search.lower()

    recipes = utils.load_valid_recipes(directory)
    matching_recipes = []
    for recipe in recipes:
        # tags and recipe names could contain uppercase or lowercase so we need to normalise them before
        # trying to find matches
        normalised_tags = [tag.lower() for tag in recipe['tags']]
        normalised_names = recipe['name'].lower().split()

        if search in normalised_tags or search in normalised_names:
            tags = ', '.join(sorted(recipe['tags']))
            matching_recipes.append((recipe['name'], recipe['source'], tags))

    return sorted(matching_recipes)

def get_recipe_tags(directory):
    """
    Get all unique recipe tags and the recipes which use them. Used as helper utility for cleaning
    up. Using defaultdict is a shortcut to ensuring we don't end up with duplicate keys, or clean
    up the results later.
    """
    recipes = utils.load_valid_recipes(directory)
    master_tags = collections.defaultdict(list)
    for recipe in recipes:
        for tag in recipe['tags']:
            master_tags[tag].append(recipe['name'])

    # Tabulate doesn't handle dictionaries well, so we convert this to a list of tuples
    # so we can print the output cleanly.
    normalised_tags = [(k, "\n".join(v)) for k, v in master_tags.items()]
    return normalised_tags
