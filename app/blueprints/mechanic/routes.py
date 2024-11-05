from flask import Blueprint, request, jsonify
from .schemas import mechanic_schema, mechanics_schema, login_mechanic_schema
from marshmallow import ValidationError
from app.models import Mechanic, db
from sqlalchemy import select
# from flask import current_app
from app.utils.util import encode_token, token_required, admin_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import limiter  # Import the limiter instance

mechanic_bp = Blueprint('mechanic', __name__)

# CREATE Mechanic
@mechanic_bp.route("/", methods=['POST'])
# @admin_required # turn on after initial creation 
def create_mechanic():
    try:
        mechanic_data = mechanic_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    pwhash = generate_password_hash(mechanic_data['password'])
    new_mechanic = Mechanic(
        name=mechanic_data['name'],
        email=mechanic_data['email'],
        phone=mechanic_data['phone'],
        salary=mechanic_data['salary']
    )
    db.session.add(new_mechanic)  
    db.session.commit()  

    return mechanic_schema.jsonify(new_mechanic), 201  

# RETRIEVE Mechanics
@mechanic_bp.route("/", methods=["GET"])
@limiter.limit("10 per hour")  # Use the imported limiter instance
def get_mechanics():
    print("GETTING MECHANICS")
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    print(page, page_size)
    query = select(Mechanic)
    if page and page_size:
        mechanics = db.paginate(query, page=int(page), per_page=int(page_size))
    else:
        mechanics = db.session.execute(query).scalars().all()

    return mechanics_schema.jsonify(mechanics), 200

# RETRIEVE SPECIFIC Mechanic localhost//1
@mechanic_bp.route("/<int:mechanic_id>", methods=['GET'])
def get_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)

    return mechanic_schema.jsonify(mechanic), 200

# UPDATE Mechanic
@mechanic_bp.route("/<int:mechanic_id>", methods=['PUT'])
@admin_required
def update_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)

    if mechanic is None:
        return jsonify({"message": "invalid id"}), 400
    
    try:
        mechanic_data = mechanic_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    for field, value in mechanic_data.items():
        if value:
            setattr(mechanic, field, value)

    db.session.commit()
    return mechanic_schema.jsonify(mechanic), 200

# DELETE Mechanic
@mechanic_bp.route("/<int:mechanic_id>", methods=['DELETE'])
@admin_required
def delete_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanic, mechanic_id)

    if mechanic is None:
        return jsonify({"message": "invalid id"}), 400

    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": f"successfully deleted mechanic {mechanic_id}!"})

# Returns the most popular mechanics
@mechanic_bp.route("/popular", methods=["GET"])
def popular_mechanics():
    query = select(Mechanic)
    mechanics = db.session.execute(query).scalars().all()

    # Sort based on popularity
    mechanics.sort(key=lambda mechanic: len(mechanic.serviceTicket), reverse=True)

    return mechanics_schema.jsonify(mechanics[:10]), 200

# Search Mechanic using name as a search term
@mechanic_bp.route("/search", methods=['GET'])
def search_mechanic():
    name = request.args.get("name")
    if name:
        query = select(Mechanic).where(Mechanic.name.like(f"%{name}%"))
    else:
        query = select(Mechanic)

    mechanics = db.session.execute(query).scalars().all()

    return mechanics_schema.jsonify(mechanics), 200

@mechanic_bp.route("/login", methods=['POST'])
def login():
    try:
        creds = login_mechanic_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    query = select(mechanic).where(mechanic.email == creds['email'])
    mechanic = db.session.execute(query).scalars().first()

    if mechanic and check_password_hash(mechanic.password, creds['password']):
        token = encode_token(mechanic.id)

        response = {
            "message": " You're are logged in",
            "status": "Success",
            "token": token
        }
    
    return jsonify(response), 200