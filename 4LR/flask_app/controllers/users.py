from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt#this enables you to encrypt you passwords
bcrypt = Bcrypt(app)

@app.route('/')#i dont nede to explain this
def index():
    return render_template('index.html')#just take you to the default room

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):#this validate register is a function that activates to determine if the information is placed correctly from the request form that is actually a dictionary that stores all the database cases
        return redirect('/')#if it fails, it goes back to the index.html for you to do again, which can activate through flash
    data ={ #if not, it will deposit all the post you made and saves them in this dectionary from the request and transfer this information to the save function where it will save the information
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])#this will encrupt your passwords when you send it out
    }
    id = User.save(data)# this will save the dictionary throught the function save which has all the new information you need to retreive
    session['user_id'] = id #i now know the id that belongs to the person personal information, it enables me to customize for the users
    return redirect('/dashboard')#then it will redirect you back to the dashboard route wich 

@app.route('/login',methods=['POST'])#if you decidede to login, it will first receive the post information you made, then 
def login():
    user = User.get_by_email(request.form)#
    if not user:#if the user doesnt match
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):#if ENCRYPTED password does not work from the check_password_hash function, it will return flash
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id#
    return redirect('/dashboard')#if it goes well, it will redirect you back to dashboard where you will be in your account

@app.route('/dashboard')#this is the route that takes you to the dashboard 
def dashboard():
    if 'user_id' not in session:#ASSUMING THAT THE USER ID IS NOT THERE, IT WILL BREAK AND LOG YOU OUT WHERE IT WILL JUST SEND YOU BACK TO THE DEDAULT PAGE AND CLEAR THE ACTION
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data))#IF NOT IT WILL JUST SEND YOU TO THE DASHBOARD PAGE, WHER THE INFORMATION YOU BEGIN TO RETREIVE FROM THE GET BY ID FUNCTION WILL FOWARD THE ID FROM THE FUNCTION AND IT WILL BE REVEALED

@app.route('/logout')#just logs you out. nothing crazy
def logout():
    session.clear()
    return redirect('/')