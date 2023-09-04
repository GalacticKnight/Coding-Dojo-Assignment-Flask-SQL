from flask import render_template, redirect, session,request#THIS IS NEEDED SO YOU CAN HAVE THESE FEATURES INTO THE FILE
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return redirect('/user/LoginRegister')#THIS IS USED TO REDIRECTED THE DEFAULT SCREEN

@app.route('/user/LoginRegister')#base route
def creation():
    return render_template("LoginAndRegister.html")

@app.route('/user/login', methods=['POST'])#this activates when you login
def loging():
    if not User.validate_login(request.form):#reuqest.form retreives all the method[post]!!!!!!!
        return redirect('/user/LoginRegister')
    session["user_id"]=User.find_by_email(request.form).id#why we need .id? because it was throwing an entire class. but it just needed a id!!!!!!!
    return redirect('/recipe/dashboard')
    
@app.route('/user/register', methods=['POST'])#this activates when you register
def registering():
    if not User.validate_register(request.form):#reuqest.form retreives all the method[post]!!!!!!!
        return redirect('/user/LoginRegister')
    data= {#we need to create a dictionary of these features in order to hash the password!!!!!!!!!!
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session["user_id"]=User.create_account(data)#returns the id of the account and saves it into a session and it will be the active account in that page!!!!
    #this session will be always activate untill you clear the session!!!!!
    return redirect('/recipe/dashboard')
    #session is more global which is why we use session instead of dictionary
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/user/LoginRegister')