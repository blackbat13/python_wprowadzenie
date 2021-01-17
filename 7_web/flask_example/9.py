from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "adfk3l5k3lkasdlk5l34wka5l"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chinook.db"

db = SQLAlchemy(app)


class playlists(db.Model):
    PlaylistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120))

    def __init__(self, name):
        self.Name = name


@app.route("/")
def index():
    return render_template("9.html", playlists=playlists.query.all())


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        if not request.form["name"]:
            flash("Name is required", "error")
        else:
            playlist = playlists(request.form["name"])
            db.session.add(playlist)
            db.session.commit()

            flash("Success")
            return redirect(url_for("index"))

    return render_template("9_add.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
