# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:20:47 2017

@author: enzo7311
"""

#==============================================================================
# from flask import Flask
# app = Flask(__name__)
# 
# @app.route("/")
# def hello():
#     return "Hello World!"
# 
# if __name__ == "__main__":
#      
#     app.run()
#==============================================================================
from flask import Flask, request, abort
from pymongo import MongoClient
from bson.json_util import dumps, default
db = MongoClient().nobel_prize
def get_country_data():

    query_dict = {}
    for key in ['country', 'category', 'year']: 
        arg = request.args.get(key) 
        if arg:
            query_dict[key] = arg

    winners = db.winners_clean.find(query_dict)
    print(winners)
 #   if winners:
 #       return dumps(winners) 
 #   abort(404) # resource not found

   
def get_country_data_():

    client = MongoClient() 
    db = client.nobel_prize 

    query_dict = {}
    coll=db['test']
#    for key in ['country', 'category', 'year']: 
#        arg = request.args.get(key) 
#        if arg:
#            query_dict[key] = arg

    winners = list(coll.find({'year':{'$gt':1980}}))
    print(winners)    