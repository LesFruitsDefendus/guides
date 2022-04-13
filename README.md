# Guides (new generation)

Les Fruits Défendus pickleaders and Saskatoon users guides.

Online version of the guides (work in progress): [French](http://lesfruitsdefendus.readthedocs.io/fr/latest), [English](http://lesfruitsdefendus.readthedocs.io/en/latest).

## Contribute to the guides

The guides website is built using [Sphinx](https://www.sphinx-doc.org/en/master/tutorial/index.html). 

The source file can be either [Markdown](https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html#intro-writing) (``.md``) or [ReStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (``.rst``) files.

### Build documentation site

To build the documentation sites, run:

```
tox -e docs
```

To serve the English documentation site, run:
```
python3 -m http.server -d ./build/docs/en
```

To serve the French documentation site, run:
```
python3 -m http.server -d ./build/docs/fr
```

### Update translation files

After modifications, update translation files:

```
tox -e trans
```

### Translate the files

The translation files are located into the [``docs/source/_locales/fr/LC_MESSAGES``](https://github.com/LesFruitsDefendus/guides/tree/master/docs/source/_locales/fr/LC_MESSAGES) folder. 
You can directly edit the ``.po`` files or use an editor.

### Test the documentation

Build the documentation sites and fail on warnings

```
tox -e testdocs
tox -e testdocs-fr
```

### Build statuses

English site: [![Documentation Status](https://readthedocs.org/projects/lesfruitsdefendus/badge/?version=latest)](https://readthedocs.org/projects/lesfruitsdefendus/)

French site: [![Documentation Status](https://readthedocs.org/projects/lesfruitsdefendus-fr/badge/?version=latest)](https://readthedocs.org/projects/lesfruitsdefendus-fr/)
