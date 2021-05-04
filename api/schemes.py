from . import ma

class HumanSchema(ma.Schema):
    class Meta:
        fields = ("name", "age")

human_schema = HumanSchema()
humans_schema = HumanSchema(many=True)
