from flask import Blueprint, request, jsonify

serviceTicket_bp = Blueprint('serviceTickets', __name__)

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
