import datetime

from Flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.datetime.now().strftime("%c")

    return 'Hello, World!' + today

@app.route('/about')
def about():
    return 'About'
