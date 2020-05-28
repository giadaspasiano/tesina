import sphinx_material

# Register the theme as an extension to generate a sitemap.xml
# extensions.append('sphinx_material')
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}
project = 'La Musica'
release = ''

author = u'Giada Spasiano - III F'

show_authors = True
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'La Musica.tex', project, author, 'manual'),
]
latex_elements = {
    'extraclassoptions': 'openany,oneside',
    'releasename': 'Scuola Media Salvemini - A.S. 2019/2020'
}
epub_basename = u'La Musica'
# Choose the material theme
html_theme = 'sphinx_material'
#html_theme = 'sphinx_materialdesign_theme'
# Get the them path
html_theme_path = sphinx_material.html_theme_path()
# Register the required helpers for the html context
html_context = sphinx_material.get_html_context()
copyright = "2020 Giada Spasiano"
html_show_sourcelink = False
html_favicon = "favicon.ico"
html_logo = "logo.png"
latex_logo = 'logo.png'
html_title = "Home"
smartquotes = False
language = "it"
# The master toctree document.
master_doc = 'index'
source_suffix = ['.rst','.md']
html_sidebars = {
    '**': ['localtoc.html', 'globaltoc.html', 'sourcelink.html', 'searchbox.html']
}
# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
templates_path = ['_templates']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/extra.css',
    'css/hacks.css',
    'css/material.css'
]
extensions = [
    'sphinxcontrib.images',
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "sphinx_markdown_tables",
    'sphinx.ext.githubpages'
]
html_theme_options = {
    'base_url': 'https://giadaspasiano.github.io/tesina',
    'repo_url': 'https://github.com/giadaspasiano/tesina/',
    'repo_name': 'giadaspasiano/tesina',
    'nav_title': 'La Musica',
    'html_minify': True,
    'css_minify': True,
    'version_dropdown': False,
    'globaltoc_depth': 5,
    # Set the color and the accent color
    'color_primary': 'indingo',
    'color_accent': 'light-blue'
}
