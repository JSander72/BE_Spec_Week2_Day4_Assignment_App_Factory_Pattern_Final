from flask import Flask
from .models import db
from app.extensions import ma, Cache, limiter
# from app.blueprints import customer, serviceTicket, mechanic
from app.blueprints.customer import customer_bp
from app.blueprints.mechanic import mechanic_bp
from app.blueprints.serviceTicket import serviceTicket_bp
# from app.extensions import limiter
from flask_limiter.util import get_remote_address



def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    app.register_blueprint(customer_bp, url_prefix="/customer")
    app.register_blueprint(serviceTicket_bp, url_prefix="/serviceTicket")
    app.register_blueprint(mechanic_bp, url_prefix="/mechanic") 

    # limiter = limiter(
    #     app,
    #     key_func=get_remote_address,
    #     default_limits=["25 per day", "2 per hour"],
    #     storage_uri="memory://",
    # )
    
   
    
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    Cache.init_app(app)  

    

    return app