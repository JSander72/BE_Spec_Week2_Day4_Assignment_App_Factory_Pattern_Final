import pytest
from flask import Flask, jsonify
from app.blueprints.serviceTicket.routes import create_new_serviceTicket, serviceTicket_bp
from app.models import ServiceTicket, Mechanic, db
from unittest.mock import patch

# FILE: app/blueprints/serviceTicket/test_routes.py


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(serviceTicket_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_new_serviceTicket_success(client):
    data = {
        "customer_id": 1,
        "mechanic_ids": [1, 2]
    }
    with patch('app.models.Mechanic.query.get') as mock_get:
        mock_get.side_effect = [Mechanic(id=1), Mechanic(id=2)]
        response = client.post("/", json=data)
        assert response.status_code == 201
        assert response.json == "New service ticket has been added to our database."

def test_create_new_serviceTicket_missing_customer_id(client):
    data = {
        "mechanic_ids": [1, 2]
    }
    response = client.post("/", json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Customer ID is required."}

def test_create_new_serviceTicket_missing_mechanic_ids(client):
    data = {
        "customer_id": 1
    }
    response = client.post("/", json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Mechanic IDs are required."}

def test_create_new_serviceTicket_invalid_mechanic_id(client):
    data = {
        "customer_id": 1,
        "mechanic_ids": [1, 99]
    }
    with patch('app.models.Mechanic.query.get') as mock_get:
        mock_get.side_effect = [Mechanic(id=1), None]
        response = client.post("/", json=data)
        assert response.status_code == 400
        assert response.json == {"error": "Mechanic with ID 99 not found."}