"""
A basic starter app  with the Flask framework and PyMongo
"""
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"


@app.route('/hello/<name>')
def saymyname(name):
    return "Hello %s" % name



if __name__ == '__main__':
    app.run(debug = True)
