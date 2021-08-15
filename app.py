# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:35:46 2021

@author: Md. Sohrawordi
"""
from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')










if __name__ == "__main__": 
    app.run() 
