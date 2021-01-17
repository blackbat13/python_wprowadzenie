from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("5.html", page=1)


@app.route("/hello/<name>")
def hello_name(name):
    return render_template("5.html", page=2, name=name)


@app.route("/prices")
def prices():
    fruits = {"apple": 2.50, "banana": 3.99, "orange": 4.55}
    return render_template("5.html", page=3, prices=fruits)


if __name__ == "__main__":
    app.run(debug=True)
