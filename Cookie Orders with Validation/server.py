from flask_app import app
from flask_app.controllers import cookie_orders#this enables you to control the routes this import is in controllers

if __name__ == "__main__":
    app.run(debug=True)