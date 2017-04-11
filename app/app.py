"""
A basic starter app  with the Flask framework and PyMongo
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT']='27017'
app.config['MONGO_DBNAME']="lsdda"

# connect to MongoDB with the defaults
#mongo    = PyMongo(app)

mongo = PyMongo(app,config_prefix='MONGO')




@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def aboutUs():
    return render_template("aboutus.html")


@app.route('/contact')
def getcontactUs():
    return render_template("contactus.html")


@app.route('/contact', methods=["POST"])
def postcontactUs():

        name = request.form['inputName']
        email = request.form['inputEmail']
        comments = request.form['textAreaComments']

        data = {
        "name": name,
         "email":email,
         "comments": comments
        }

        try:
            mongo.db.contactUs.insert_one(data)
            return redirect(url_for('all_comments'))
        except err:
            return "Inesrt Failed: Something wentwrong"
        #return jsonify(result=data);

        #return render_template("contactResponse.html",result=data)


@app.route('/comments')
def all_comments():
    comments = mongo.db.contactUs.find()
    return render_template("comments.html", comments=comments)





if __name__ == '__main__':
    app.run(debug = True)
