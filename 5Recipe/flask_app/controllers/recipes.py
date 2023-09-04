from flask import render_template, redirect, session, request#THIS IS NEEDED SO YOU CAN HAVE THESE FEATURES INTO THE FILE
from flask_app import app 
from flask_app.models.user import User#you want to add this so you can use the methods in models!!!!!!
#p.models.user you need to specify that you want it in the user file in model!!!!!!!!
from flask_app.models.recipe import Recipe

@app.route('/recipe/dashboard')
def dashboard():
    data=User.find_by_id({"id":session["user_id"]})#this will activate the current session you made that you named session["user_id"] in line 19 of users.py!!!!!!
    #in the id that you restreive from the table, you create a dictionary with the id of what you got from the table, and that is what you registering
    retreiving_all_recipes =Recipe.get_all()
    return render_template('dashboard.html',user=data, recipes =retreiving_all_recipes)#when ever you use {{user.asdasdasd}}, its becasuse of the word user in user=data!!!!!!

@app.route('/recipes/create')#this takes you to the page wherer you can add your recipes
def add_recipe():
    #VVVVV we need this again!!!!!
    data=User.find_by_id({"id":session["user_id"]})#this will activate the current session you made that you named session["user_id"] in line 19 of users.py!!!!!!

    return render_template("add_recipe.html",users=data)


@app.route('/recipes/add_recipe',methods=["POST"])#while this registers the recipe you added
def adding_recipe():
    if not Recipe.validate_recipe(request.form):#reuqest.form retreives all the method[post]!!!!!!!
        return redirect('/recipes/create')
    Recipe.save(request.form)#before we had to use a dictionary because we need to manipulate the data, but here we can just save the data and send you back to the dashboard!!!!!
    #which is why wee needed the save function!!!!
    return redirect("/recipe/dashboard")#takes you back to the dashboard that you created all the recipes so far


@app.route('/recipes/view_recipe/<int:id>')
def view_recipe(id):
    recipe_info= Recipe.find_by_id({"id":id})#you are trying to find the recipe by the recipe id!!!!!
    you = User.find_by_id({"id":session["user_id"]})
    return render_template("view_recipe.html",recipes=recipe_info, users=you)


@app.route('/recipes/edit_recipe/<int:id>')#<int:id> this is your recipe id abd you are passing it to the find by id!!!!!!!!!!
def edit_recipe(id):
    recipe_info= Recipe.find_by_id({"id":id})#you are trying to find the recipe by the recipe id!!!!!
    you = User.find_by_id({"id":session["user_id"]})
    return render_template("edit_recipe.html",recipes=recipe_info, users=you)


@app.route('/recipes/editing_recipe',methods=["POST"])
def editing_recipe():


    if not Recipe.validate_recipe(request.form):#reuqest.form retreives all the method[post]!!!!!!!
        return redirect(f'/recipes/edit_recipe/{request.form["id"]}')#!!!!!!!!!!????????????
    Recipe.update(request.form)


    return redirect("/recipe/dashboard")


@app.route('/recipes/delete/<int:id>')#%(user_id)s is the id in the parameter!!!!!!!!
def delete_recipe(id):#something is in here i just dont know what
    
    Recipe.delete({"id":id})#the colored id is receiving the id from the route <int:id>!!!!!!!!
    return redirect("/recipe/dashboard")