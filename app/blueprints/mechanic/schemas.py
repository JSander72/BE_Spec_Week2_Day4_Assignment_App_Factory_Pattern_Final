from app.models import Mechanic
from app.extensions import ma



class MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        include_fk = True

mechanics_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)