from app.models import Customer
from app.extensions import ma
from marshmallow import fields


class Customerschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
    serviceTickets = fields.Nested("ServiceTicketSchema", many=True)

customer_schema = Customerschema()
customers_schema = Customerschema(many=True)
login_schema = Customerschema(exclude=["phone", "name", "role"])