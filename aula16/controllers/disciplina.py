from flask import request, Blueprint, Response

from aula16.models.model import db, Disciplina
import json

app = Blueprint("disciplina", __name__)

@app.route("/")
def index():
    disciplinas = Disciplina.query.all()
    result = [e.to_dict() for e in disciplinas]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route("/list", methods=["GET"])
@app.route("/list/<int:limit>", methods=["GET"])
def lista(limit=1):
    rows = db.session.execute("select id,nome from Disciplina limit "+str(limit)+"").fetchall()
    result = [dict(r) for r in rows]
    print(json.dumps(result))
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route("/view/<int:id>", methods=["GET"])
def view(id):
    row = db.session.execute("select id,nome from Disciplina where id= %s" %id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")

@app.route("/add", methods=["POST"])
def add():
    disciplina = Disciplina(request.form['nome'])
    db.session.add(disciplina)
    db.session.commit()
    return Response(response=json.dumps({'status':'success','data':disciplina.to_dict()}), status=200, content_type="application/json")

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    disciplina = Disciplina.query.get(id)
    db.session.delete(disciplina)
    db.session.commit()
    return Response(response=json.dumps(disciplina.to_dict()), status=202, content_type="application/json")

@app.route("/edit/<int:id>", methods=["PUT","POST"])
def edit(id):
    disciplina = Disciplina.query.get(id)
    disciplina.nome = request.form['nome']
    db.session.commit()
    return Response(response=json.dumps(disciplina.to_dict()), status=202, content_type="application/json")