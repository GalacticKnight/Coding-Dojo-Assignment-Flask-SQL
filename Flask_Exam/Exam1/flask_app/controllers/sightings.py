from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.sighting import Sighting
from flask import flash

@app.route("/sightings/dashboard")
def dashboard():
    if "user_id" not in session:#activates when there is a fail with whether the account exist which could be interpret as a crash if you skip to this page.
        flash("You must be logged in to access the dashboard.")
        return redirect("/")
    
    user = User.get_by_id(session["user_id"])
    sightings = Sighting.get_all()
    #this saves the dictionary when you get the user by id and retrieves all the database and send it to the dashboard html that shows all the sightings
    return render_template("sighting.html", user=user, sightings=sightings)

@app.route("/sightings/<int:sighting_id>")
def showing_details(sighting_id):
    user = User.get_by_id(session["user_id"])
    sighting = Sighting.get_by_id(sighting_id)
    return render_template("show.html", user=user, sighting=sighting)

@app.route("/sightings/create")
def create_new_sighting():
    return render_template("new_sighting.html")

@app.route("/sightings", methods=["POST"])
def createing_new_sighting():
    valid_sighting = Sighting.create_valid_sighting(request.form)#test to see if the new sighting is valid 
    if valid_sighting:#if true
        return redirect(f'/sightings/{valid_sighting.id}')
    return redirect('/sightings/create')#otherwise it will take you back to create a new sighitng and you have to redo again

@app.route("/sightings/edit/<int:sighting_id>")#the number here will be the sighting id which will indicate which row in the table to update
def edit_sighting(sighting_id):
    sighting = Sighting.get_by_id(sighting_id)
    return render_template("edit_sighting.html", sighting=sighting)


@app.route("/sightings/<int:sighting_id>", methods=["POST"])#the number here will be the sighting id which will indicate which row in the table to update
def update_sighting(sighting_id):
    valid_sighting = Sighting.update_sighting(request.form, session["user_id"])
    if valid_sighting:
        return redirect(f"/sightings/{sighting_id}")
    return redirect(f"/sightings/edit/{sighting_id}")

@app.route("/sightings/delete/<int:sighting_id>")#the number here will be the sighting id which will indicate which row in the table to delete
def delete_by_id(sighting_id):
    Sighting.delete_sighting_by_id(sighting_id)
    return redirect("/sightings/dashboard")