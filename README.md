# Website

Based on this [jekyll theme](https://github.com/alshedivat/al-folio)

## Local preview

```
$ bundle exec jekyll serve
```

## Publications

- Export from paperpile
- convert from bib to json with pandoc (see `_bibliography/json2yaml.py`)
- Remove `''` from yaml file with `sed`
- Final should be in `_data/publications.yaml`

## Deploy

Use depoly script to deploy to `gh-pages`. Netlify takes care of the rest.

```
$ ./bin/deploy
```
