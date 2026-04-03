from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("demo2.html")

@app.route("/p")
def p():
    return render_template("jikosyoukai.html")

@app.route("/h")
def h():
    return render_template("hobby.html")

