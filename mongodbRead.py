# -*- coding: utf-8 -*-
import pandas as pd

from pymongo import MongoClient

client = MongoClient() 
db = client.nobel_prize 
print(db)
coll=db['test']
#res=coll.find({'category':'Chemistry'})
res=coll.find({'year':{'$gt':1980}})
print(list(res))
