# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 18:45:55 2017

@author: enzo7311
"""
import pandas as pd

from pymongo import MongoClient

client = MongoClient() 
db = client.nobel_prize 

mia=pd.read_json('nobel_winners_biopic.json')
 
records = mia.to_dict('records')
db["winners"].insert(records)

   