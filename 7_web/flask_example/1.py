# Najpierw importujemy stosowne moduły z bilbioteki flask, którą należy zainstalować poleceniem pip install flask
from flask import Flask

# Tworzymy nową instancję aplikacji Flask
app = Flask(__name__)


# Aplikacja Flask składa się głównie z metod odpowiadających poszczególnym endpointom
@app.route('/')
def hello_world():
    return "Witaj!"


@app.route('/hello/')
def hello():
    return "<h1>Hello</h1>"


if __name__ == "__main__":
    # Uruchamiamy aplikację w trybie debugowania - dzięki temu zmiany w kodzie będą na bieżąco odtwarzane po stronie aplikacji
    app.run(debug=True)
