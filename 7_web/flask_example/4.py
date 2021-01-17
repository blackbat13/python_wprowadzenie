from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("4.html")


@app.route("/admin")
def hello_admin():
    return "Welcome Admin"


@app.route("/guest/<name>")
def hello_guest(name):
    return f"Hello dear guest {name}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["login"]
    else:
        user = request.args.get("login")

    if user == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", name=user))


if __name__ == "__main__":
    app.run(debug=True)
