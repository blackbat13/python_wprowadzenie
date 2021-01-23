from flask import Flask

app = Flask(__name__)


# W endpointach możemy także podawać parametry
@app.route("/hello/<name>/ab")
def hello_name(name):
    return f"Hello {name}"


# Możemy także zdefiniować typ paramteru
@app.route("/show/<int:number>")
def show_int(number):
    return f"Your lucky integer for today is {number}"


# Aplikacja automatycznie dopasuje przekazaną wartość do podanego typu
@app.route("/show/<float:number>")
def show_float(number):
    return f"Your lucky float for today is {number}"


if __name__ == "__main__":
    app.run(debug=True)
