from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("Home_Page.html")

@app.route("/login")
def login():
    return render_template("LOgin.html")

@app.route("/signup")
def signup():
    return render_template("Signup.html")

@app.route("/downloads")
def download():
    return render_template("Download.html")

