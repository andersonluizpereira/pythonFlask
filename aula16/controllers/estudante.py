from flask import request, Blueprint, Response

from aula16.models.model import Estudante,db
import json

app = Blueprint("estudante", __name__)

@app.route("/")
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route("/list", methods=["GET"])
@app.route("/list/<int:limit>", methods=["GET"])
def lista(limit=1):
    rows = db.session.execute("select id,nome,idade from Estudante limit "+str(limit)+"").fetchall()
    result = [dict(r) for r in rows]
    print(json.dumps(result))
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route("/view/<int:id>", methods=["GET"])
def view(id):
    row = db.session.execute("select id,nome,idade from Estudante where id= %s" %id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")

@app.route("/add", methods=["POST"])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return Response(response=json.dumps({'status':'success','data':estudante.to_dict()}), status=200, content_type="application/json")

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=202, content_type="application/json")

@app.route("/edit/<int:id>", methods=["PUT","POST"])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=202, content_type="application/json")