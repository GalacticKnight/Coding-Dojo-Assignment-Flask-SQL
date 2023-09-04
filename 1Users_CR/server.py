from flask import Flask, render_template, redirect, request

# import the class from friend.py
from users import User#users is the users.py and the second User is from the class

app = Flask(__name__)
@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    return render_template("users.html", users=User.get_all())

@app.route("/users/new")
def new_users():
    return render_template('new_user.html')


@app.route("/users/new",methods=['POST'])
def new():
    User.save(request.form)#IMPORTANT ********************************
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)