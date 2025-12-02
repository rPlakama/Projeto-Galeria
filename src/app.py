from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mariadb+mariadbconnector://rPlakama:jaquksww@localhost/Galeria"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Artista(db.Model):
    __tablename__ = "artistas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    resumo = db.Column(db.Text, nullable=False)
    ano_inicio = db.Column(db.Integer)
    ano_fim = db.Column(db.Integer)
    nacionalidade = db.Column(db.String(255))
    lore_link = db.Column(db.Text, nullable=False)


class Obras(db.Model):
    __tablename__ = "obras"
    id = db.Column(db.Integer, primary_key=True)
    artista_id = db.Column(db.Integer, db.ForeignKey("artistas.id"), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    link_image = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    ano = db.Column(db.Integer)
    artista = db.relationship("Artista", backref="obras")


@app.route("/")
def index(name=None):
    obras = Obras.query.all()
    return render_template("index.html", obras=obras)


@app.route("/obras")
def obras():
    obras = Obras.query.all()
    return render_template("obras.html", obras=obras)


@app.route("/artistas")
def artistas():
    nome_artista = request.args.get("nome")
    ano_inicio_filtro = request.args.get("ano_inicio")
    ano_fim_filtro = request.args.get("ano_fim")

    query = Artista.query

    if nome_artista:
        query = query.filter(Artista.nome.ilike(f"%{nome_artista}%"))

    if ano_inicio_filtro and ano_fim_filtro:
        query = query.filter(
            Artista.ano_inicio >= int(ano_inicio_filtro),
            Artista.ano_fim <= int(ano_fim_filtro)
        )

    artistas = query.all()

    return render_template("artistas.html", artistas=artistas)


@app.route("/add_artista", methods=["GET", "POST"])
def add_artista():
    if request.method == "GET":
        lista_artistas = Artista.query.all()
        return render_template("add_artista.html", artistas=lista_artistas)

    if request.method == "POST":
        novo_artista = None
        try:
            nome_artista = request.form.get("nome")
            ano_inicio = request.form.get("ano_inicio")
            ano_fim = request.form.get("ano_fim")
            resumo_artista = request.form.get("resumo")
            nacionalidade_artista = request.form.get("nacionalidade")
            lore_link = request.form.get("link")

            if (
                not nome_artista
                or not ano_inicio
                or not ano_fim
                or not nacionalidade_artista
                or not resumo_artista
                or not lore_link
            ):
                return (
                    "Todos os objetos são obrigatórios",
                    400,
                )

            novo_artista = Artista(
                lore_link=lore_link,
                nome=nome_artista,
                ano_inicio=int(ano_inicio),
                ano_fim=int(ano_fim),
                resumo=resumo_artista,
                nacionalidade=nacionalidade_artista,
            )
            db.session.add(novo_artista)
            db.session.commit()

            return redirect(url_for("artistas"))

        except Exception as e:
            db.session.rollback()
            return f"Um erro inesperado ocorreu: {e}", 500


@app.route("/add", methods=["GET", "POST"])
def add_art():
    if request.method == "GET":
        artistas = Artista.query.all()
        return render_template("add_art.html", artistas=artistas)

    if request.method == "POST":
        nova_obra = None
        try:
            nome_obra = request.form.get("nome")
            ano_obra = request.form.get("ano")
            desc_obra = request.form.get("desc")
            link_obra = request.form.get("link_image")
            artista_id_obra = request.form.get("artista_id")

            if not nome_obra or not link_obra or not artista_id_obra:
                return (
                    "Erro: Nome da Obra, Link da Imagem e Artista são obrigatórios.",
                    400,
                )

            ano_int = int(ano_obra) if ano_obra else None
            artista_id_int = int(artista_id_obra)

            nova_obra = Obras(
                nome=nome_obra,
                desc=desc_obra,
                ano=ano_int,
                link_image=link_obra,
                artista_id=artista_id_int,
            )

            db.session.add(nova_obra)
            db.session.commit()

            return redirect(url_for("index"))

        except ValueError:
            db.session.rollback()
            return "Erro: O 'Ano' ou 'ID do Artista' parece ser inválido.", 400

        except Exception as e:
            db.session.rollback()
            return f"Um erro inesperado ocorreu: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
