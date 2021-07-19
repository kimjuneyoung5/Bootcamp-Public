from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def display_ninjas():
    return render_template("ninjas/index.html", all_dojos = Dojo.get_all())


@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)

    return redirect("/dojos")


##@app.route("/dojos/<int:dojo_id>")
##def display_dojo(dojo_id):
##    return render_template("dojos/display.html", dojo = Dojo.get_one({"id":dojo_id}))
##
