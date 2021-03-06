from flask import Flask, render_template, url_for, request, session, redirect,flash,logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MONGO_DBNAME'] = 'helpdesk'
app.config['MONGO_URI'] = 'mongodb+srv://test:test@episupt-tasga.gcp.mongodb.net/helpdesk?retryWrites=true&w=majority'

mongo = PyMongo(app)


from login import *
from profile import *
from ticket import *
from admin import *
from ticketadmin import *
from incidencias import *
from usuarioincidencia import*

#@app.route('/')
#def index():
 #   return render_template('index.html')


if __name__ == '__main__':
    app.run()
