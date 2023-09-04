from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.cookie_order import Cookie_order

@app.route("/")# THIS REDIRECTS
def start():
    return redirect("/cookies")

@app.route("/cookies")#THIS IS THE MAIN ENTRY SITE THAT SHOWS ALL THE COOKIES 
def index():
    # get all the orders
    orders = Cookie_order.get_all()#THIS GET ALL FUNCTION FROM LINE 47 IN MODELS REVEALS ALL THE ORDERS
    return render_template("cookies.html", orders=orders)

    # def get_all(cls):# this is use to reveal all the orders in a row
    #     query = "SELECT * from cookie_orders;"
    #     orders_data = connectToMySQL(cls.DB).query_db(query)
    #     orders = []
    #     for order in orders_data:
    #         orders.append(cls(order))
    #     return orders


@app.route("/cookies/new")# IF YOU WANT TO MAKE A NEW COOKIE ORDER, THIS WILL THROW YOU TO THE NEW OREDER HTML THAT WILL ENABLE YOU TO ADD A COOOKIE
def new_page():
    return render_template("new_order.html")
    # <form action="/cookies" method="post">
    # in this form, you will post straight to the 
    # @app.route("/cookies", methods=["POST"])


@app.route("/cookies", methods=["POST"])#activates from new order html
def create_cookie():
    cookie_order = request.form #you need this to get inputs from forms
    print(request.form)
    if not Cookie_order.is_valid(cookie_order):#THIS RUNS THE VALID TEST TO DETERMINE IF THE ORDER YOU MADE IS LEGIT IF NOT IT WILL RETURN TO THE NEW ORDER 
        return redirect("/cookies/new")#sends you back to remake in the new_order.html
    Cookie_order.create(cookie_order)#OTHERWISE, IT WILL CREATE THE ORDER IN LINE 56 OF MODELS AND RETURN YOU TO THE MAIN ORDER
    return redirect("/")

    # def create(cls, cookie_order):
    #     query = """ INSERT into cookie_orders (name, cookie_type, num_boxes) VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s);"""
    #     result = connectToMySQL(cls.DB).query_db(query, cookie_order)
    #     return result

@app.route("/cookies/edit/<int:cookie_id>")# THIS IS IS THE UPDATE FEATURE IN CRUD. THAT WILL ENABLE YOU TO (first) HAVE ACCESS TO THE PAGE OF THE EDIT OREDER
def edit_page(cookie_id):
    order = Cookie_order.get_by_id(cookie_id)#THIS REFERS TO THE METHOD IN THE CLASS COOKIE ORDER IN THE MODEL FILE TO GET THE ID AND SAVE IT AS ORDER
    return render_template("edit_order.html", order = order)#THIS ACTIVATES THE ORDER FILE AND SENDS THE INFORMATION OF ORDER WHICH IS THE ID



@app.route("/cookies/edit/<int:cookie_id>", methods=["POST"])
def update_cookie(cookie_id):
    cookie_order = request.form#resquest form is a definition is immutable, it puts a name as a key and every other contents you put is the 
    if not Cookie_order.is_valid(cookie_order):
        return redirect(f"/cookies/edit/{cookie_id}")
    Cookie_order.update(cookie_order)
    return redirect("/")



@app.route("/cookies/delete/<int:cookie_id>")# THIS IS IS THE UPDATE FEATURE IN CRUD. THAT WILL ENABLE YOU TO (first) HAVE ACCESS TO THE PAGE OF THE EDIT OREDER
def delete(cookie_id):
    cookie_order = request.form
    Cookie_order.delete(cookie_order)#THIS REFERS TO THE METHOD IN THE CLASS COOKIE ORDER IN THE MODEL FILE TO GET THE ID AND SAVE IT AS ORDER
    return render_template("edit_order.html")



#request.form{
# "name:value"
# }