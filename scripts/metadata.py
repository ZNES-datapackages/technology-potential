#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run this script in the root directory of the datapackage to get metadata
from data
"""
from datapackage import Package, infer

# get meta data with infer function
descriptor = infer('data/**/*.csv')

print(descriptor)

# create package based on derscriptor
p = Package(descriptor)

# add key 'name' to desrciptor with value 'tech...'
p.descriptor['name'] = 'Potentials for energy system modelling per EU country'

p.descriptor["contributors"] = [{
        "title": "'Simon Hilpert'",
        "email": "simon.hilpert@uni-flensburg.de",
        "role": "author"
    },
   {
        "title": "Martin Soethe",
        "email": "martin.soethe@uni-flensburg.de",
        "role": "author"
    }
]

p.descriptor["sources"] = [
    {
        "title": "DLR",
        "path": "https://elib.dlr.de/77976/1/REMix_Thesis_YS.pdf"
    },
    {
        "title": "Brown & Schlachtberger",
        "path": "https://doi.org/10.5281/zenodo.1146665"
    },
    {
        "title": "LIMES-EU",
        "path": "https://www.pik-potsdam.de/research/sustainable-solutions/models/limes/DocumentationLIMESEU_2014.pdf"
    },
    {
        "title": "zfes",
        "path": "http://www.zfes.uni-stuttgart.de/deutsch/downloads/20120727_Final_Stromspeicherpotenziale_fuer_Deutschland-.pdf"
    },
    {
        "title": "hotmaps",
        "path": "https://gitlab.com/hotmaps/potential"
    }
]

p.commit()

p.save('datapackage.json')
