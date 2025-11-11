from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mariadb+mariadbconnector://rPlakama:jaquksww@localhost/Galeria"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def index(name=None):
    return render_template("index.html", person=name)


@app.route("/artistas")
def artistas():
    artistas = Artista.query.all()
    return render_template("artistas.html", artistas=artistas)


class Artista(db.Model):
    __tablename__ = "artistas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    periodo_atuacao = db.Column(db.String(255))
    nacionalidade = db.Column(db.String(255))


class Obra(db.Model):
    __tablename__ = "obras"
    id = db.Column(db.Integer, primary_key=True)
    artista_id = db.Column(db.Integer, db.ForeignKey("artistas.id"), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    link_image = db.Column(db.String(255), nullable=False)
    ano = db.Column(db.Integer)
