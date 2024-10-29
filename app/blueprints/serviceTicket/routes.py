from flask import Blueprint, request, jsonify

serviceTicket_bp = Blueprint('serviceTickets', __name__)
tickets = {}
mechanics = {}

@serviceTicket_bp.route('/serviceTickets', methods=['GET'])
def get_serviceTickets():
    return jsonify({"message": "List of service tickets"})

@serviceTicket_bp.route('/serviceTickets', methods=['POST'])
def create_serviceTicket():
    data = request.get_json()
    return jsonify({"message": "Service ticket created", "data": data}), 201

@serviceTicket_bp.route('/serviceTickets/<int:ticket_id>', methods=['PUT'])
def update_serviceTicket(ticket_id):
    data = request.get_json()
    return jsonify({"message": f"Service ticket {ticket_id} updated", "data": data})

@serviceTicket_bp.route('/serviceTickets/<int:ticket_id>', methods=['DELETE'])
def delete_serviceTicket(ticket_id):
    return jsonify({"message": f"Service ticket {ticket_id} deleted"})

@serviceTicket_bp.route('/serviceTickets/<int:ticket_id>/add_mechanic_id>', methods=['PUT'])
def add_mechanic_to_ticket(ticket_id, mechanic_id):
    ticket = tickets.get(ticket_id)
    if ticket:
        mechanic = mechanics.get(mechanic_id)
        if mechanic:
            ticket["mechanics"].append(mechanic)
            return jsonify({"message": f"Mechanic {mechanic_id} added to ticket {ticket_id}", "ticket": ticket})
        else:
            return jsonify({"message": "Mechanic not found"}), 404
    else:
        return jsonify({"message": "Ticket not found"}), 404