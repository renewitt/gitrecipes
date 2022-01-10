# GitRecipes

GitRecipes is a little library which allows you to store and manage your recipes in git.
<br/><br/> 
  
## Get Started  
All you need to get started is a python virtualenv with gitrecipes installed, and a folder with some recipes in it. You can check out the source, or look in the examples folder to see how to format your recipes.

```
$ python -m venv
$ pip install gitrecipes

$ gitrecipes new-index
$ gitrecipes index
```
<br />

## Commands
| Command | Description |
| --- | --- |
| `gitrecipes new-index` | Create a new recipes directory with an example recipe |
| `gitrecipes list` | List all recipes indexed by gitrecipes |
| `gitrecipes new-recipe AnzacBiscuits` | Create a new blank recipe template called AnzacBiscuits in the recipes directory |
| `gitrecipes publish html` | Publish all recipes in a static browsable set of html files |
| `gitrecipes publish pdf` | Publish all recipes in a printable format |
| `gitrecipes for chicken` | List the recipes are tagged with `chicken` as an ingredient, or the recipes which have `chicken` in the recipe name |  
| `gitrecipes tags` | List all the recipe tags you have, and the recipes which use them |  

<br />  

## Configuration
The CLI tools expect a directory with recipes in it. If you run `gitrecipes new-index`, a folder called `recipes` will be created in your current directory. If you have checked out the `gitrecipes` source and you want to keep your recipes separate, all the CLI commands allow you to pass in a custom directory as an option with `--directory`. If you get tired of this, you can also export an environment variable which `gitrecipes` will respect as your preferred directory.
```
export GITRECIPES_DIRECTORY='/home/Documents/recipes'
```

## Managing Recipes
To create a new recipe, run `gitrecipes new-recipe <RecipeName>`. 
Recipe file names can be any case, but should not contain whitespaces. They can contain separating characters like `-` and `_`. 
The full recipe name in the yaml file should be named with whitespaces instead of separating characters.

`gitrecipes new-recipe IcedWater` or `gitrecipes new-recipe iced-water` or `gitrecipes new-recipe iced-water`
```yaml
# IcedWater.yml/iced-water.yml/iced-water.yml
---
name: Iced Water
source: Family Recipe
tags:
  - sides
  - cold
```

### Tagging
Searching using `gitrecipes for` also checks the name of the recipe for matching strings, so you don't need to double up on tags. While labelling is personal choice, it's recommended that less tags makes for a more managable recipe index.

For example:
A recipe called `Chocolate Cake` does not need to be tagged with `chocolate`, or `cake`. A search for `gitrecipes for cake` would return this recipe due to the name. More relevant tags might be `sweet` or `dessert`.

### Ignoring Recipes
Sometimes you want recipes to be saved, but you don't like them anymore, or don't care about them. If you're using source control, you could always delete them and get them back later, or you can use the `!` character to ignore. Any recipe name which starts with `!` will be ignored during indexing or searching.

## Future Development
GitRecipes is a work in progress. Here are some of the features that are in development or are planned for the future.
* Be able to search for recipes by ingredient, time to prepare or source
* Be able to categorise recipes and list by category
* Be able to store more complex recipes which may have multiple components - eg. a cake with icing
* Try to find a better solution than `pdfkit` for creating print ready documents. It's very slow and has system install dependencies.
* Be able to generate one printable recipe at a time, instead of doing all of them
<br/><br/>
  
## FAQ:
*Why yaml?*  
YAML is both easy to machine parse, and also pretty human readable. YAML files can be easily parsed and displayed in many other formats, while also leaving you the option of being able to easily read the raw file and check the necessary ingredients while you're at the shop.
<br/><br/> 
  
## Dependencies
To create PDFs, you will need to install `PDFKit` in your virtual environment. `PDFKit` is already defined as a dependency for gitrecipes, but in order for it to run correctly, you will also need to install `wkhtmltopdf`. You can find instructions on how to get `wkhtmltopdf` running on your distribution [here](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf).