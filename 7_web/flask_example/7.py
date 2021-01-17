from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/setcookie/<name>")
def set_cookie(name):
    resp = make_response("OK")  # Tworzymy nową odpowiedź na zapytanie
    resp.set_cookie("userName", name)  # Dodajemy nowe cisteczko do odpowiedzi
    return resp


@app.route("/getcookie")
def get_cookie():
    name = request.cookies.get("userName")  # Pobieramy ciasteczko z zapytania
    return f"Cookie userName: {name}"


if __name__ == "__main__":
    app.run(debug=True)
