from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
	eamil = request.form.get("email")
	password = request.form.get("password")
	return render_template("login.html")

@auth.route("/signup",  methods=['GET', 'POST'])
def signup():
	eamil = request.form.get("email")
	username = request.form.get("username")
	password_1 = request.form.get("password_1")
	password_2 = request.form.get("password_2")
	return render_template("signup.html")

@auth.route("/logout", methods=['GET', 'POST'])
def logout():
	return redirect(url_for("views.home"))