from flask import render_template, redirect, request#THIS IS NEEDED SO YOU CAN HAVE THESE FEATURES INTO THE FILE
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojo')#THIS IS USED TO REDIRECTED THE DEFAULT SCREEN INTO THE /DOJOS PAGE

@app.route('/dojo')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",all_dojos = dojos)

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojo')

@app.route('/delete/dojo/<int:dojo_id>')
def delete_dojos(dojo_id):
    print("A")
    print(dojo_id)
    data={#we need this because the agorithm requires a mapping
        'dojo_id': dojo_id
    }
    Dojo.delete(data)
    return redirect("/dojo")

@app.route('/update/dojo', methods=['POST'])
def update_dojos():
    Dojo.update(request.form)
    return render_template("update_dojo.html")

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))