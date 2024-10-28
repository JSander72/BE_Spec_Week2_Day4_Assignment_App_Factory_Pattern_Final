from flask import Flask
from .models import db
from .extensions import ma
from .blueprints.customer.routes import customer_bp
from .blueprints.serviceTicket.routes import serviceTicket_bp
from .blueprints.mechanic.routes import mechanic_bp



def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'sqlite:///mechanic.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from .models import Customer, ServiceTicket, Mechanic

   
        app.register_blueprint(customer_bp, url_prefix="/customers")
        app.register_blueprint(serviceTicket_bp, url_prefix="/service_tickets")
        app.register_blueprint(mechanic_bp, url_prefix="/mechanics")

    return app