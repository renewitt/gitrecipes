""" Main CLI entry point for gitrecipes. """

import click
import yaml
import jinja2
import pathlib

import gitrecipes.create
import gitrecipes.manage
import gitrecipes.validate

from gitrecipes import LOGGER

@click.group()
def cli_options():
    """ Run a command to manage your gitrecipes. """
    pass

@click.command()
@click.option('--directory', type=str, default='recipes')
def new_index(directory):
    gitrecipes.create.new_index(directory)

@click.command()
@click.argument('recipe_name')
@click.option('--directory', type=click.Path(exists=True), default='recipes')
def new_recipe(directory, recipe_name):
    """
    Create a new recipe.
    A new basic template recipe will be created in the configured directory.
    """
    gitrecipes.create.new_recipe_template(directory, recipe_name)

@click.command()
@click.option('--directory', type=click.Path(exists=True), default='recipes')
def index(directory):
    """
    Look in the default or configured directory for readable recipes and return
    an alphabetised list.
    """
    recipes = gitrecipes.manage.list_all_recipes(directory)
    if recipes:
        click.echo('----------')
        click.echo('Here are all your available recipes:')
        for recipe in recipes:
            LOGGER.info(f"  - {recipe}")

@click.command()
@click.argument('publish_format', type=click.Choice(['html', 'pdf']))
@click.option('--directory', type=click.Path(exists=True), default='recipes')
def publish(directory, publish_format):
    """
    Publish the recipes in the configured format.
    """
    if publish_format == 'pdf':
        gitrecipes.manage.publish_print(directory)
        click.echo(f'Published recipes are ready for print in `pdf/`')
        return

    if publish_format == 'html':
        gitrecipes.manage.publish_html(directory)
        click.echo(
            f'Your recipes have been published and are ready for browsing in `html/`')
        return


cli_options.add_command(new_index)
cli_options.add_command(new_recipe)
cli_options.add_command(index)
cli_options.add_command(publish)

def main():
    """
    This method is the main CLI entry point to gitrecipes.
    """
    cli_options()
