from flask import Flask, g

import forms
import models

Debug = True

app = Flask(__name__)
app.secret_key = "shrreasfass781!-adffa1"


@app.before_request
def befor_request():
    """Connect to the Database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the Database after each request"""
    g.db.close()
    return response

@app.route('/')

@app.route('/entries')

@app.route('/entries/new')

@app.route('/entries/<id>')

@app.route('/entries/<id>/edit')

@app.route('/entries/<id>/delete')
