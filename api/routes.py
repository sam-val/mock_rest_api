from api import app, db
from flask import request, jsonify
from api.models import Human
from .schemes import human_schema, humans_schema


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

    return human_schema.dump(new_human)
    

