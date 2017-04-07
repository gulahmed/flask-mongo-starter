"""
A basic starter app  with the Flask framework and PyMongo
"""
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def aboutUs():
    return render_template("aboutus.html")

@app.route('/contact', methods=["GET","POST"])
def contactUs():
    if(request.method == "GET"):
        return render_template("contactus.html")
    elif (request.method == "POST"):
        name = request.form['inputName']
        email = request.form['inputEmail']
        comments = request.form['textAreaComments']

        data = {
        "name": name,
         "email":email,
         "comments": comments
        }

        return render_template("contactResponse.html",result=data)




@app.route('/hello/<name>')
def saymyname(name):
        return render_template("index.html",name=name)



if __name__ == '__main__':
    app.run(debug = True)
