from flask import Flask
app = Flask(__name__)
app.secret_key = "Very tired"

from flask_app.controllers import users