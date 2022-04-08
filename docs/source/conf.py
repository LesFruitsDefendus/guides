# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Les Fruits Défendus'
copyright = '2022, Les Fruits Défendus'
author = 'Les Fruits Défendus'

# The full version, including alpha/beta/rc tags
release = '2022.x'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.spelling",
    "recommonmark",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Configure spell checker.
spelling_word_list_filename = 'spelling_wordlist.txt'

# Translations
locale_dirs = ['_locales/'] 
gettext_compact = False 
spelling_lang = os.getenv('SPHINX_SPLELLING_LANG') or 'en_US'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# html_title = "Your title"
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"

# Theme options
html_theme_options = {
    "repository_url": "https://github.com/LesFruitsDefendus/guides",
    "path_to_docs": "docs/",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "logo_only": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 3,
    "announcement": "Work in progress...",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
