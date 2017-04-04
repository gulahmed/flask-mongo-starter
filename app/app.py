"""
A basic starter app  with the Flask framework and PyMongo
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def aboutUs():
    return render_template("aboutus.html")

@app.route('/contact')
def contactUs():
    return render_template("contactus.html")



@app.route('/hello/<name>')
def saymyname(name):
        return render_template("index.html",name=name)



if __name__ == '__main__':
    app.run(debug = True)
