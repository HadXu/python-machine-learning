# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:59:36 2015

@author: hadxu
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('first_app.html')
    
if __name__=='__main__':
    app.run()