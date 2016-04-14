from flask import render_template
from application import app

@app.route('/health', methods=["GET"])
def check_status():
    return status

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/signin', methods=["GET"])
def signin():
    return render_template('signin.html')

@app.route('/signup', methods=["GET"])
def signup():
    return render_template('signup.html')

@app.route('/profile', methods=["GET"])
def profile():
    return render_template('profile.html')
