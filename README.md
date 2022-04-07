# Guides

Les Fruits Défendus pickleaders and Saskatoon users guides.

Online version of the guides (work in progress): http://lesfruitsdefendus.readthedocs.io/

[![Documentation Status](https://readthedocs.org/projects/lesfruitsdefendus/badge/?version=latest)](https://readthedocs.org/projects/lesfruitsdefendus/)


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

### Test the documentation

Build the documentation sites and fail on warnings

```
tox -e testdocs
```
