# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:31:22 2017

@author: enzo7311
"""

import requests

response = requests.get('http://localhost:8000/api/winners',\
                         params={"category": "Physiology or Medicine"})

response.json()