import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div style=\"text-align: center;\"><h1>Hello World!</h1><p>Welcome to my GCP DevOps Project.</p><p>This a Simple Flask application</p></div>'