import pathlib

import pytest
import yaml

TEST_RESOURCES = 'resources'
@pytest.fixture(scope='function')
def load_recipe():
    """ Load a recipe file and return the contents as YAML. """
    def _load(recipe_file):
        parent_dir = pathlib.Path(__file__).parent.absolute()
        path = pathlib.Path(parent_dir / f"{TEST_RESOURCES}/{recipe_file}")
        return yaml.safe_load(path.read_text())
    yield _load
