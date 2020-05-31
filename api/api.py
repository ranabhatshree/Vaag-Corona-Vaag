# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:28:33 2020

@author: Shree K. Ranabhat
"""

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/api/subscribe', methods=['GET'])
def home():
    return "You can Subscribe Me here!"

app.run()
