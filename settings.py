# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:25:25 2017

@author: enzo7311
"""
#api/settings.py

# Optional MONGO variables
#MONGO_HOST = 'localhost'
#MONGO_PORT = 27017
#MONGO_USERNAME = 'user'
#MONGO_PASSWORD = 'user'
X_DOMAINS='*'
HATEOS=False
PAGINATION=False
URL_PREFIX = 'api'
MONGO_DBNAME = 'nobel_prize'
DOMAIN = {'winners':{
    'item_title': 'winners',
    'schema':{
        'country':{'type':'string'},
        'category':{'type':'string'},
        'name':{'type':'string'},
        'year':{'type': 'integer'},
        'gender':{'type':'string'},
        'mini_bio':{'type':'string'}, 
        'bio_image':{'type':'string'}
        },
    'url':'winners' 
}}
  