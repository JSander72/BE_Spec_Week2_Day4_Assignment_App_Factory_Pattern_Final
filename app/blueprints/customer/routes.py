from flask import request, jsonify
from app.blueprints.customer import customer_bp
from .schemas import customer_schema, customers_schema, login_schema
from marshmallow import ValidationError
from app.models import Customer, db
from sqlalchemy import select
from app.extensions import limiter
from app.utils.util import encode_token, token_required
from werkzeug.security import generate_password_hash, check_password_hash

# Login Customer
@customer_bp.route("/login", methods=['POST'])
def login():
    # Validate the payload and ensure they sent us email and password
    try:
        creds = login_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    query = select(Customer).where(Customer.email == creds['email'])
    customer = db.session.execute(query).scalars().first()

    if customer and check_password_hash(customer.password, creds['password']):  # If we have a customer associated with the email, and the password is the same
        token = encode_token(customer.id, customer.role)
        response = {
            "message": "successfully logged in",
            "status": "success",
            "token": token
        }
        return jsonify(response), 200
    
    return jsonify({"message": "Invalid credentials"}), 401

# CREATE Customer
@customer_bp.route("/", methods=['POST'])
# @limiter.limit("3 per hour")
def create_customer():
    # Validate and deserialize incoming data
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    # If data is valid, create new customer with that data
    pwhash = generate_password_hash(customer_data['password'])
    new_customer = Customer(
        name=customer_data['name'],
        email=customer_data['email'],
        phone=customer_data['phone'],
        password=pwhash,
        role=customer_data['role']
    )
    db.session.add(new_customer)  # Add to session
    db.session.commit()  # Commit session to db

    return customer_schema.jsonify(new_customer), 201  # Return new_customer object as a response

# RETRIEVE Customers
@customer_bp.route("/", methods=["GET"])
def get_customers():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()

    return customers_schema.jsonify(customers), 200

# RETRIEVE SPECIFIC Customer
@customer_bp.route("/<int:customer_id>", methods=['GET'])
def get_customer(customer_id):
    customer = db.session.get(Customer, customer_id)

    return customer_schema.jsonify(customer), 200

# UPDATE CUSTOMER
@customer_bp.route("/", methods=['PUT'])
@token_required
def update_customer(token_user):
    customer = db.session.get(Customer, token_user)

    if customer is None:
        return jsonify({"message": "Invalid ID"}), 400
    
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    for field, value in customer_data.items():
        if value:
            setattr(customer, field, value)

    db.session.commit()
    return customer_schema.jsonify(customer), 200

# DELETE CUSTOMER
@customer_bp.route("/", methods=['DELETE'])
# @limiter.limit("3 per hour")
@token_required
def delete_customer(token_user):
    customer = db.session.get(Customer, token_user)

    if customer is None:
        return jsonify({"message": "Invalid ID"}), 400

    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted customer {token_user}!"})
