from flask import render_template
from application import app

@app.route("/health")
def check_status():
    return "Status OK"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')
