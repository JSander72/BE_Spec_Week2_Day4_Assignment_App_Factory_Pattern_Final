from app.models import ServiceTicket
from app.extensions import ma



class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        include_fk = True

serviceTicket_schema = ServiceTicketSchema()
serviceTickets_schema = ServiceTicketSchema(many=True)
# input_serviceTicket_schema = ServiceTicketSchema(exclude=['service_date', 'mechanics'])


