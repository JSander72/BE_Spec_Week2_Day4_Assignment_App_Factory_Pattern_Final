from flask import Blueprint, request, jsonify

mechanic_bp = Blueprint('mechanic', __name__)

@mechanic_bp.route('/mechanics', methods=['GET'])
def get_mechanics():
    return jsonify({"message": "List of mechanics"})

@mechanic_bp.route('/mechanics', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    return jsonify({"message": "Mechanic created", "data": data}), 201

@mechanic_bp.route('/mechanics/<int:mechanic_id>', methods=['PUT'])
def update_mechanic(mechanic_id):
    data = request.get_json()
    return jsonify({"message": f"Mechanic {mechanic_id} updated", "data": data})

@mechanic_bp.route('/mechanics/<int:mechanic_id>', methods=['DELETE'])
def delete_mechanic(mechanic_id):
    return jsonify({"message": f"Mechanic {mechanic_id} deleted"})