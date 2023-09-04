from flask import render_template, redirect, session,request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/user/LoginRegister')
