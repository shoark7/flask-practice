import flask
from flask import Flask, url_for, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'asdfasdf' * 5


@app.route('/users/<username>')
def echo_username(username):
    return username + ', hi!'


@app.route('/request')
def request_test():
    return str(dir(request))


@app.route('/flask')
def flask_test():
    return str(dir(flask))
