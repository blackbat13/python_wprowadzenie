from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/setcookie/<name>")
def set_cookie(name):
    resp = make_response("OK")
    resp.set_cookie("userName", name)
    return resp


@app.route("/getcookie")
def get_cookie():
    name = request.cookies.get("userName")
    return f"Cookie userName: {name}"


if __name__ == "__main__":
    app.run(debug=True)
