""" Functionality used to validate recipes on import. """

import cerberus

# This schema describes the nodes a recipe is expected to have and defines
# the format the yaml files are expected to be in for proper handling.
# The only mandatory nodes are: `name, ingredients and method`
RECIPE_SCHEMA = {
    'name': {
        'required': True,
        'type': 'string'
    },
    'source': {
        'required': False,
        'type': 'string',
        'nullable': True
    },
    'serves': {
        'required': False,
        'type': 'integer',
        'nullable': True
    },
    'minutes_prep_time': {
        'required': False,
        'type': 'integer',
        'nullable': True
    },
    'minutes_cook_time': {
        'required': False,
        'type': 'integer',
        'nullable': True
    },
    'description': {
        'required': False,
        'type': 'string',
        'nullable': True
    },
    'ingredients': {
        'required': True,
        'minlength': 1,
        'type': ['list', 'dict']
    },
    'method': {
        'required': True,
        'minlength': 1,
        'type': ['list', 'dict']
    },
    'notes': {
        'required': False,
        'type': 'list',
        'nullable': True
    }
}

def validate_recipe(recipe):
    """ Use cerberus and the above schema to check if a recipe is in the expected format. """
    validator = cerberus.Validator(RECIPE_SCHEMA)
    res = validator.validate(recipe)
    return res
