from app.extensions import ma
from app.models import Customer

class Customerschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True

customer_schema = Customerschema()
input_customer_schema = Customerschema()
customer_schema = Customerschema(many=True)