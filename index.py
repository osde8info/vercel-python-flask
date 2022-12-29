from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        "home.html",
        name="yourname",
        date=datetime.now()
    )


@app.route("/about/")
def about():
    return render_template(
        "about.html"
    )


@app.route("/contact/")
@app.route("/contact/<name>")
def contact(name=None):
    return render_template(
        "contact.html",
        name=name,
        date=datetime.now()
    )
