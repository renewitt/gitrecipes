
"""
Generate a new gitrecipes index and add a basic recipe into it. Running this command
creates all the folder and enough example data to run the rest of the commands.
"""
import pathlib
import yaml

import gitrecipes.utils as utils

TEMPLATE = {
    'name': None,
    'source': None,
    'tags': ['tag1', 'tag2'],
    'serves': 0,
    'minutes_prep_time': 0,
    'minutes_cook_time': 0,
    'description': None,
    'ingredients': ['first ingredient'],
    'method': ['first step'],
    'notes': ['first note']
}

def represent_none(self, _):
    """
    Add custom yaml representer/handler to write out Python None values as empty strings.
    """
    return self.represent_scalar('tag:yaml.org,2002:null', '')

yaml.add_representer(type(None), represent_none)

def _write_yaml_file(path, content):
    """
    Write the yaml content to the path.

    :param path: pathlib object to file
    :path content: python dictionary with yaml content
    """
    path.write_text(yaml.dump(
        content,
        sort_keys=False,
        width=85,
        explicit_start=True))

def new_recipe_template(directory, recipe_name):
    """
    Create a new blank recipe template in the configured directory.

    :param directory: Directory where new recipe template will be created
    :param recipe_name: Name of the template to create
    """
    # Check if this recipe already exists before creating it
    new_recipe = pathlib.Path.cwd() / directory / f"{recipe_name}.yml"
    if new_recipe.exists():
        utils.LOGGER.error(f"Recipe {recipe_name} already exists in {directory}.")
        return 1

    _write_yaml_file(new_recipe, TEMPLATE)
    utils.LOGGER.info(f'Successfully created new recipe {recipe_name}')

def new_index(directory):
    """ Create a new gitrecipes index in the current directory. """
    recipe_index = pathlib.Path.cwd() / directory
    if recipe_index.exists():
        utils.LOGGER.error(f'Directory `{directory}/` already exists, cannot run setup.')
        return 1

    recipe_index.mkdir()
    utils.LOGGER.info(f'Created a new gitrecipes index in {recipe_index}.')
    _write_example_recipe(recipe_index)

def _write_example_recipe(recipe_index):
    """ Write a basic recipe to the newly created index. """
    recipe = {
        'name': 'Iced Water',
        'source': ' a family recipe',
        'tags': [
            'cold',
            'side',
            'ice'
        ],
        'serves': 2,
        'prep_time': '2 minutes',
        'cook_time': 0,
        'description': (
            'This drink is an old classic enjoyed by many, kids and adults. This will be sure to '
            'please especially on a hot day. Similar to water, but much more refreshing, this '
            'drink can go with just about anything.'
        ),
        'ingredients': [
            '2 cups fresh clear water',
            '3-5 ice cubes',
            'lime (optional)'
        ],
        'method': [
            'Delicately place ice cubes in a tall glass, as not to break them.',
            'Shake glass from side to side as to allow the ice to settle in the bottom of the glass.',
            'Evenly fill the glass with the water. You will notice a cracking noise (this is normal).',
            'Wait about one minute for ice to chill the water.',
            'In the meantime rinse the lime and cut into wedges.',
            (
                'Make an incision on the inside of one wedge and place over the side of the glass. '
                'Or just place a few lime wedges directly inside the glass if you prefer.'
            )
        ],
        'notes': [
            'Lime can be substituted with lemon if desired',
            'If you experience pain due to sensitive teeth, you can use a straw'
        ]
    }
    recipe_file = pathlib.Path(recipe_index / 'IcedWater.yml')
    _write_yaml_file(recipe_file, recipe)
    utils.LOGGER.info(f"Run `gitrecipes index` to see all your recipes!")