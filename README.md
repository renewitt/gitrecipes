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
| `gitrecipes with chicken` | (WIP) List the recipes which contain `chicken` as an ingredient |  

<br />  

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
YAML is both easy to machine parse, and also pretty human readable. YAML files can be easily parsed and displayed in many other formats, while also leaving you the option of being able to easily read the raw file and check the necessary ingredients while you're at the shops.
<br/><br/> 
  
## Dependencies
To create PDFs, you will need to install `PDFKit` in your virtual environment. `PDFKit` is already defined as a dependency for gitrecipes, but in order for it to run correctly, you will also need to install `wkhtmltopdf`. You can find instructions on how to get `wkhtmltopdf` running on your distro [here](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf).