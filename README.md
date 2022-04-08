# Guides

Les Fruits Défendus pickleaders and Saskatoon users guides.

Online version of the guides (work in progress): [French](http://lesfruitsdefendus.readthedocs.io/fr/), [English](http://lesfruitsdefendus.readthedocs.io/en/)

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
You can directly edit the ``.po`` files or use a editor.

### Test the documentation

Build the documentation sites and fail on warnings

```
tox -e testdocs
```

### Build statuses

English site: [![Documentation Status](https://readthedocs.org/projects/lesfruitsdefendus/badge/?version=latest)](https://readthedocs.org/projects/lesfruitsdefendus/)

French site: [![Documentation Status](https://readthedocs.org/projects/lesfruitsdefendus-fr/badge/?version=latest)](https://readthedocs.org/projects/lesfruitsdefendus-fr/)
