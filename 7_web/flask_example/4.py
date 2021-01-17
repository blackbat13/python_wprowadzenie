from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# Aby korzystać z szablonów html, powinny one znajdować się w katalogu templates
@app.route("/")
def index():
    return render_template("4.html")


@app.route("/admin")
def hello_admin():
    return "Welcome Admin"


@app.route("/guest/<name>")
def hello_guest(name):
    return f"Hello dear guest {name}"


# Dana metoda może być przypisana do kilku typów zapytań HTTP i jej zachowanie może się różnić w zależności od typu zapytania
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
