from app.models import Mechanic
from app.extensions import ma



class Mechanicschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        include_fk = True

mechanics_schema = Mechanicschema()
# input_mechanics_schema = Mechanicschema()
mechanics_schema = Mechanicschema(many=True)