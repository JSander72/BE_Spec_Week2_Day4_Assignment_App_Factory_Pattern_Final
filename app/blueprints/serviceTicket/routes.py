from app.blueprints import serviceTicket
from .schemas import ServiceTicketSchema, ServiceTicketsSchema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import ServiceTicket, db
from sqlalchemy import select
from datetime import date, datetime
from app.extensions import Limiter, Cache
from app.utils.util import admin_required



serviceTicket_bp = serviceTicket.serviceTicket_bp

@serviceTicket_bp.route("/", methods =['POST'])
def create_new_serviceTicket():
    try: 
        serviceTicket_data = ServiceTicketSchema.load(request.json) 
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_serviceTicket = ServiceTicket(vin=serviceTicket_data['vin'], service_date=serviceTicket_data['service_date'], service_desc=serviceTicket_data['service_desc'], customer_id = serviceTicket_data['customer_id'])
    db.session.add(new_serviceTicket) 
    db.session.commit()

    return jsonify("new service ticket has been added our database."), 201


@serviceTicket_bp.route("/", methods =['GET'])
def get_serviceTicket():
    query = select(ServiceTicket)
    serviceTickets = db.session.execute(query).scalars().all()

    return ServiceTicketSchema.jsonify(serviceTickets), 200



@serviceTicket_bp.route ("/<int:service_ticket_id>", methods=['GET'])
def get_service_ticket(serviceTicket_id):
    serviceTicket = db.session.get(ServiceTicket, serviceTicket_id )

    return ServiceTicketSchema.jsonify(serviceTicket), 200


@serviceTicket_bp.route("/<int:serviceTicket_id>", methods =['PUT'])
def update_service_ticket(serviceTicket_id):
    service_ticket = db.session.get(ServiceTicket, serviceTicket_id)

    if serviceTicket== None:
        return jsonify ({"message": "invalid id"}), 400
    
    try:
        serviceTicket_data = ServiceTicketSchema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    for field, value in serviceTicket_data.items():
        if value:
            setattr(service_ticket, field, value)

    db.session.commit()
    return ServiceTicketSchema.jsonify(serviceTicket), 200



@serviceTicket_bp.route("/<int:service_ticket_id>", methods=['DELETE'])
def delete_serviceTicket(serviceTicket_id):
    serviceTicket = db.session.get(ServiceTicket, serviceTicket_id)

    if serviceTicket == None:
        return jsonify({"message": "invalid id"}), 400

    db.session.delete(serviceTicket)
    db.session.commit()
    return jsonify({"message": f"User at ID {serviceTicket_id}  has been deleted "})
