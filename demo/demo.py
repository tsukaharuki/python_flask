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

@app.route("/r")
def r():
    return render_template("research.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

