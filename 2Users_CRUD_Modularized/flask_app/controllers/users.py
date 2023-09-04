from flask import render_template,redirect,request,session

from flask_app import app#this is the only way to use the term app so this is very important

from flask_app.models.user import User#users is the users.py and the second User is from the class


@app.route("/")
def index():
    return redirect('/user')

@app.route("/user")
def users():
    return render_template("user.html", users=User.get_all())#IMPORTANT ********************************

@app.route("/user/new")
def new_users():
    return render_template('new_user.html')


@app.route("/user/new",methods=['POST'])
def new():
    User.save(request.form)#IMPORTANT ********************************
    return redirect('/user')