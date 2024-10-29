from flask import Flask
from app.models import db
from app.extensions import ma, Limiter, Cache
from app.blueprints.customer.routes import customer_bp
from app.blueprints.serviceTicket.routes import serviceTicket_bp
from app.blueprints.mechanic.routes import mechanic_bp



def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    
   
    db.init_app(app)
    ma.init_app(app)
    Limiter.init_app(app)
    Cache.init_app(app)  

    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(serviceTicket_bp, url_prefix="/service_tickets")
    app.register_blueprint(mechanic_bp, url_prefix="/mechanics")

        

    return app