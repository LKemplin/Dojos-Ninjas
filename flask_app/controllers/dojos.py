from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route("/")
def all_dojos():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template("index.html", dojos=dojos)

@app.route("/create_new_dojo", methods=["POST"])
def create_new_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.create_dojo(data)
    return redirect("/")

@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos=dojos)

@app.route("/show_dojo/<int:dojo_id>")
def show_dojo(dojo_id):
    data = {"dojo_id": dojo_id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojos.html", dojo=dojo)
