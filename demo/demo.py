from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/h")
def h():
    return render_template("demo.html")

