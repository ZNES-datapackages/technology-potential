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
p.descriptor['name'] = 'Renewable and Storage Potential'

p.descriptor['description'] = "Renewable Energy and Storage Potential per Country"

p.descriptor["contributors"] = [{
    "title": "'Simon Hilpert'",
    "email": "simon.hilpert@uni-flensburg.de",
    "role": "author"
    }
]

p.descriptor["sources"] = [{
    "title": "DLR",
    "path": "https://elib.dlr.de/77976/1/REMix_Thesis_YS.pdf"
    },
    {
    "title": "ZNES",
    "path": "ZNES_2050_ehighway"
    }
]

p.commit()

p.save('datapackage.json')
