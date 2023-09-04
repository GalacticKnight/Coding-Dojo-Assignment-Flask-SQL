from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask import flash

@app.route("/")
def index():
    return render_template("LR.html")

@app.route("/register", methods=["POST"])
def register():
    valid_user = User.create_valid_user(request.form)
    if not valid_user:#if the user is not valid(which returns true or false from the function above,)
        return redirect("/")#it will take you back to the login spot
    session["user_id"] = valid_user.id#otherwise, it will save your information through the user id and take you to the dashboard
    return redirect("/sightings/dashboard")

@app.route("/login", methods=["POST"])
def login():
    ###################there needs to be a way to determine if there is an account already
    session["user_id"] = valid_user.id
    return redirect("/sightings/dashboard")#if successful,it will send you to the 

@app.route("/logout")
def logout():
    session.clear()#delete the little session you made and redirects you backt to the the page that forces you to l or r
    return redirect("/")