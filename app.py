"""
Create a Flask Application
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/<name>')
def say_my_name(name):
    return 'Hello {} from SG!'.format(name)


@app.route('/debug')
def test_debug():
    var_a, var_b = 1, "test"
    raise Exception("This is a test exception")
    return "Debugging"


@app.route('/template')
@app.route('/template/<name>')
def template(name=None):
    return render_template('template.html', name=name)


@app.route("/me")
def me_api():
    return {
        "username": "tyng",
        "theme": "blue",
        "image": "www.google.com",
    }

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'