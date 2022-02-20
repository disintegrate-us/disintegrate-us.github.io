from flask import render_template, redirect, url_for, request
from forms import LoginPage_LoginForm
from dis_site import app


@app.route("/", methods=["GET", "POST"])
def login():
    loginForm = LoginPage_LoginForm(request.form)
    if request.method == 'POST' and loginForm.validate():
        return redirect(url_for("home"))
    return render_template("password.html", loginForm=loginForm)


@app.route("/home")
def home():
    return render_template("home.html")