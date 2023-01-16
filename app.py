from flask import Flask, session, render_template, request, jsonify
import requests
from pymongo import MongoClient
#Server
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/join.html')
