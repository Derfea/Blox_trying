from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("Home_Page.html")

@app.route("/Login")
def login():
    args = request.args
    age = args.get("age")
    name = args.get("name")

    return render_template("LOgin.html", name = name, age = age)

