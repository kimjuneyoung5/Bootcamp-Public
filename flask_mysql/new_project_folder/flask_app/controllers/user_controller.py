from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User


@app.route("/users")
def index():
    return render_template("index.html", all_users = User.get_all())


@app.route("/users/new")
def new_user():
    return render_template("new_user.html")


@app.route("/users/create", methods = ['POST'])
def create_user():
    # print(request.form)
    User.create(request.form)

    return redirect("/users")


@app.route("/users/<int:user_id>")
def display_user(user_id):
    return render_template("display.html", user = User.get_one({"id":user_id}))


@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    return render_template("edit_user.html", user = User.get_one({"id":user_id}))


@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    new_dict = {
        "frist_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id" : user_id
    }
    another_dict = {
        **request.form,
        "id" : user_id
    }
    User.update(another_dict)

    return redirect("/users")


@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({"id":user_id})

    return redirect("/users")
    