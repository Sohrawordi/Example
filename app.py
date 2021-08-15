# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:35:46 2021

@author: Md. Sohrawordi
"""
from flask import Flask



app = Flask(__name__)

@app.route("/")
def home():
    return "Hellow World"










if __name__ == "__main__": 
    app.run() 