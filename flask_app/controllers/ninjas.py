from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
import flask_app.models.dojo

@app.route("/new_ninja", methods=["POST"])
def add_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    return redirect (f"/show_dojo/{request.form['dojo_id']}")

