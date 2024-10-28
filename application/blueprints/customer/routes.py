from flask import Blueprint, request, jsonify

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    return jsonify({"message": "List of customers"})

@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    return jsonify({"message": "Customer created", "data": data}), 201

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    return jsonify({"message": f"Customer {customer_id} updated", "data": data})

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    return jsonify({"message": f"Customer {customer_id} deleted"})