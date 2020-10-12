""" Test recipe loading and validation functions. """
import gitrecipes.validate

def test_validation_basic(load_recipe):
    """
    Test that a basic recipe with a list of ingredients, and one method loads correctly.
    """
    recipe = load_recipe('basic_recipe.yml')
    assert gitrecipes.validate.validate_recipe(recipe)

def test_validation_complex(load_recipe):
    """
    Test that a basic recipe with a list of ingredients, and one method loads correctly.
    """
    recipe = load_recipe('complex_recipe.yml')
    assert gitrecipes.validate.validate_recipe(recipe)
