""" Functionality used to validate recipes on import. """

import cerberus

# This schema describes the nodes a recipe is expected to have and defines
# the format the yaml files are expected to be in for proper handling.
# The only mandatory nodes are: `name, ingredients, method`
# @TODO: Allow more complex recipes with multiple sets of ingredients and methods
BASIC_SCHEMA = {
    'name': {
        'required': True,
        'type': 'string'
    },
    'source': {
        'required': False,
        'type': 'string'
    },
    'serves': {
        'required': False,
        'type': 'integer'
    },
    'minutes_prep_time': {
        'required': False,
        'type': 'integer'
    },
    'minutes_cook_time': {
        'required': False,
        'type': 'integer'
    },
    'description': {
        'required': False,
        'type': 'string'
    },
    'ingredients': {
        'required': True,
        'type': 'list',
    },
    'method': {
        'required': True,
        'type': 'list',
    },
    'notes': {
        'required': False,
        'type': 'list',
    }
}

def validate_recipe(recipe):
    """ Use cerberus and the above schema to check if a recipe is in the expected format. """
    validator = cerberus.Validator(BASIC_SCHEMA)
    return validator.validate(recipe)