import re
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if "uuid" in session:
        return redirect("/success")
    
    return render_template("index.html")


@app.route("/success")
def display_success():
    if "uuid" not in session:
        flash("You must be logged in to enter this website")
        return redirect("/")

    return render_template("display.html", user = User.get_by_id({"id":session['uuid']}))

@app.route("/register", methods=['POST'])
def register_user():
    if not User.register_validate(request.form):
        return redirect("/")

    hash_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": hash_pass
    }
    user_id = User.create(data)
    session['uuid'] = user_id

    return redirect("/success")

@app.route("/login", methods = ['POST'])
def login_user():
    if not User.login_validate(request.form):
        return redirect("/")

    user = User.get_by_username({'username':request.form['username']})
    session['uuid'] = user.id

    return redirect("/success")

@app.route("/logout")
def logout_user():
    session.clear()

    return redirect("/")