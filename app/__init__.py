from flask import Flask
from app.models import db
from app.extensions import ma, Cache
from app.blueprints import customer, serviceTicket, mechanic
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address



def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
   
    limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["25 per day", "2 per hour"],
    storage_uri="memory://",
    )

    db.init_app(app)
    ma.init_app(app)
    Limiter.init_app(app)
    Cache.init_app(app)  

    app.register_blueprint(customer.customer_bp, url_prefix="/customers")
    app.register_blueprint(serviceTicket.serviceTicket_bp, url_prefix="/serviceTickets")
    app.register_blueprint(mechanic.mechanic_bp, url_prefix="/mechanics") 

    return app