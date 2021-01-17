from flask import Flask, render_template, request, flash, redirect, url_for
# Aby korzystać z modułu SQLAlchemy zintegrowanego z biblioteką flask, musimy go najpierw zainstalować
# pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "adfk3l5k3lkasdlk5l34wka5l"

# Ustawiamy url bazy danych w konfiguracji aplikacji
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chinook.db"

# Tworzymy obiekt bazy danych
db = SQLAlchemy(app)


# Definiujemy klasę odpowiadającą tabeli w bazie danych
class playlists(db.Model):
    PlaylistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120))

    def __init__(self, name):
        self.Name = name


@app.route("/")
def index():
    # Pobieramy wszystkie playlisty z bazy i przekazujemy je do szablonu
    return render_template("9.html", playlists=playlists.query.all())


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        if not request.form["name"]:
            # Używając polecenia flash możemy przekazać różne komunikaty do szablonu html
            flash("Name is required", "error")
        else:
            playlist = playlists(request.form["name"])  # Tworzymy nowy obiekt playlisty
            db.session.add(playlist)  # Dodajemy playlistę do bazy danych
            db.session.commit()  # Zapisujemy zmiany

            flash("Success")
            return redirect(url_for("index"))

    return render_template("9_add.html")


if __name__ == "__main__":
    # Tworzymy wszystkie tabele zgodnie ze zdefiniowanymi klasami, jeżeli nie ma ich jeszcze w bazie danych
    db.create_all()
    app.run(debug=True)
