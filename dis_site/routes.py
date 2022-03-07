import flask_login
from flask import render_template, redirect, url_for, request
from forms import LoginPage_LoginForm
from singleuser import User
from dis_site import app, db, loginManager
from flask_login import login_user, login_required


@app.route("/", methods=["GET", "POST"])
def login():
    loginForm = LoginPage_LoginForm(request.form)
    if request.method == 'POST' and loginForm.validate():
        user = User.query.first()
        if(user.checkPasswordHash(loginForm.password.data)):
            login_user(user=user, remember=False)
            return redirect(url_for("home"))
    return render_template("password.html", loginForm=loginForm)

@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html")

@loginManager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect(url_for("login"))