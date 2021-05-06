from api import app, db
from flask import request, jsonify, Response
from api.models import Human
from .schemes import human_schema, humans_schema
import sys


@app.route('/', methods=['GET'])
def index():
    return jsonify("Hello World")


@app.route('/add', methods=['POST'])
def add_human():
    name = request.json['name']
    age = request.json['age']

    new_human = Human(name=name, age=age)

    db.session.add(new_human)
    db.session.commit()
    x = human_schema.dump(new_human)

    print(type(x), file=sys.stderr)

    return human_schema.dump(new_human)
    
@app.route('/get/<id>', methods=['GET'])
def get_human(id):

    h = Human.query.filter_by(id=id).first()

    if h:
        return human_schema.dump(h)

    return '' # flask doesn't allow to return None, so...

@app.route('/get_all', methods=['GET'])
def get_all_humans():
    hs = Human.query.order_by(Human.name).all()

    return jsonify(humans_schema.dump(hs))

@app.route('/alter/<id>', methods=['PUT'])
def alter_human(id):
    try:
        name = request.json['name']
        age = request.json['age']
        if (isinstance(name, str) and isinstance(age, int)):
            if len(name) < 2:
                raise Exception
        else:
            raise Exception
    except:
        return "Request Json is not valid."

    h = Human.query.filter_by(id=id).first()

    h.name = name
    h.age = age

    db.session.add(h)
    db.session.commit()

    if h:
        return human_schema.dump(h)
    else:
        return "No Human Found."

@app.route('/kill', methods=['POST'])
def kill_human():
    h = Human.query.filter_by(id=request.json['id']).first()

    if h:
        db.session.delete(h)

        db.session.commit()

        return Response("Success", status=200, mimetype="text/html")
    else:
        return Response("No Human Found", status=404, mimetype="text/html")