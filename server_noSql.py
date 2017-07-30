# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:06:17 2017

@author: enzo7311
"""
 
# server_nosql.py
# server_nosql.py
from flask import Flask, request, abort
from pymongo import MongoClient
from bson.json_util import dumps, default

app = Flask(__name__)

db = MongoClient().nobel_prize

@app.route('/api/winners')
def get_country_data():

    query_dict = {}
    for key in ['country', 'category', 'year']: 
        arg = request.args.get(key) 
        if arg:
            query_dict[key] = arg

    winners = db.test.find(query_dict)
    if winners:
        return dumps(winners) 
    abort(404) # resource not found

if __name__=='__main__':
    app.run(port=8000, debug=True)