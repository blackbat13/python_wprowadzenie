from flask import Flask, request, session, redirect, url_for, render_template, abort

app = Flask(__name__)
app.secret_key = "adfk3l5k3lkasdlk5l34wka5l"


@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return render_template("8.html", username=username)
    else:
        return render_template("8.html", username=None)


@app.route("/login", methods=["POST"])
def login():
    session["username"] = request.form["username"]
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/private")
def private():
    if "username" in session:
        return "Access Granted"
    else:
        abort(401)


if __name__ == "__main__":
    app.run(debug=True)
