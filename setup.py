from setuptools import setup, find_packages

setup(
    name="gitrecipes",
    version="0.1",
    author="Rachael Elizabeth",
    description="Store and categorise your recipes in git.",
    install_requires=[
        'jinja2',
        'click',
        'pyyaml',
        'cerberus',
        'pdfkit',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'gitrecipes=gitrecipes.__main__:main'
        ],
    },
    packages=find_packages(exclude="test")
)