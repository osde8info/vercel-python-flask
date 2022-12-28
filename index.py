import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.datetime.now()

    return 'Hello, World!' + today

@app.route('/about')
def about():
    return 'About'
    