from api import db

class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __repr__(self):
        return f"Human: {self.name}, {self.age} years of age."

    