# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 17:48:03 2017

@author: enzo7311
"""
import pandas as pd
import sqlalchemy
engine=sqlalchemy.create_engine(
        'sqlite:///data/nobel_prize.db')


mia=pd.read_json('data/nobel_winners_cleaned.json')
mia.to_sql('winners',engine)
