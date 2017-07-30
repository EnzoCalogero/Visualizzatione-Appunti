# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:27:34 2017

@author: enzo7311
"""

# api/server_eve.py
from eve import Eve

app = Eve()

if __name__=='__main__':
    app.run(port=8000,debug=True)