from app.models import ServiceTicket
from app.extensions import ma



class ServiceTicketschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        include_fk = True

serviceTicket_schema = ServiceTicketschema()
input_serviceTicket_schema = ServiceTicketschema(exclude=['service_date', 'mechanics'])
serviceTicket_schema = ServiceTicketschema(many=True)

