from flask import Flask

app = Flask(__name__)


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"


@app.route("/show/<int:number>")
def show_int(number):
    return f"Your lucky integer for today is {number}"


@app.route("/show/<float:number>")
def show_float(number):
    return f"Your lucky float for today is {number}"


if __name__ == "__main__":
    app.run(debug=True)
