from flask import Flask, request, session, redirect, url_for, render_template, abort

app = Flask(__name__)
# Aby korzystać z modułu sesji, musimy zdefiniować tajny klucz aplikacji, którego nie powinniśmy nigdzie udostępniać
# Dane sesji są przechowywane w szyfrowanym ciasteczku
app.secret_key = "adfk3l5k3lkasdlk5l34wka5l"


# Z obiektu sesji korzystamy jak ze słownika
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
    session.pop("username", None)  # Usuwamy nazwę użytkownika z sesji
    return redirect(url_for("index"))


@app.route("/private")
def private():
    if "username" in session:
        return "Access Granted"
    else:
        abort(401)  # Zwracamy błąd HTTP 401 - Unauthorized


if __name__ == "__main__":
    app.run(debug=True)
