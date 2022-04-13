# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

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
    "myst_parser",
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
html_logo = "_static/lfd.png"

# JS to swicth language easily
JS_LANG = """
if (window.location.pathname.indexOf('/en/') != -1) {
    <!-- Give the user a link to this page, but in french. -->
    var link = document.getElementById('fr-docs-link');
    link.href = window.location.pathname.replace(/\/en\//, '/fr/');
    <!-- And make it visible -->
    link.style.display = "";
    delete link;
}
else{
    if (window.location.pathname.indexOf('/fr/') != -1) {
        <!-- Give the user a link to this page, but in english. -->
        var link = document.getElementById('en-docs-link');
        link.href = window.location.pathname.replace(/\/fr\//, '/en/');
        <!-- And make it visible -->
        link.style.display = "";
        delete link;
    }
}
"""

HEADER_HTML = f"""
<div style="float:left;"></div>

Work in progress... 

<div style="float:right;">
    <a href="https://saskatoon.lesfruitsdefendus.org/">Saskatoon</a>
    |
    <a id="en-docs-link" href="/en/latest/" style="display:none;">English</a>
    <a id="fr-docs-link" href="/fr/latest/" style="display:none;">Français</a>
</div>

<script type="text/javascript">
{JS_LANG}
</script>
"""

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
    "announcement": HEADER_HTML,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]
