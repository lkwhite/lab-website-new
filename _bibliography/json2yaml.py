#! /usr/bin/env python

'''
1. Export paperpile bibliography as papers.bib

2. convert papers.bib to json with:

    `pandoc papers.bib -t csljson -o papers.json`

3. convert papers.json to papers.yaml with:

    ``
'''

import simplejson
import yaml

import sys
import pdb
import collections

def main():

    json_file = sys.argv[1]
    json = simplejson.load(open(json_file))

    for entry in json:
        print(yaml.dump(create_yaml(entry)))

def authors(entry):
   
    authors = []
    for a in entry['author']:
        try:
            author = a['family'] + " " + a['given'][0]
        except KeyError:
            continue

        authors.append(author)

    return ", ".join([i for i in authors])

def create_yaml(entry):

    x = dict() 


    try:
        x['details'] = entry['container-title']
    except KeyError:
        x['details'] = ''

    try:
        x['year'] = entry['issued']['date-parts'][0][0]
    except KeyError:
        x['year'] = ''

    try:
        x['pmid'] = entry['PMID']
    except KeyError:
        x['pmid'] = ''


    try:
        x['doi'] = entry['DOI']
    except KeyError:
        x['doi'] = ''

    x['authors'] = authors(entry)
    x['title'] = entry['title']
    x['pmcid'] = ''
    x['github'] = ''
    x['biorxiv'] = ''
    x['preprint'] = ''

    return [x]

if __name__ == "__main__":
    main()
