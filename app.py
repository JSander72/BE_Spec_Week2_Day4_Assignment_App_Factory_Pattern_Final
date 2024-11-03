from app import create_app
from app.models import db
from app.blueprints import customer, serviceTicket, mechanic

app = create_app('DevelopmentConfig')

# app.register_blueprint(customer.customer_bp, url_prefix="/customers")
# app.register_blueprint(serviceTicket.serviceTicket_bp, url_prefix="/serviceTickets")
# app.register_blueprint(mechanic.mechanic_bp, url_prefix="/mechanics") 

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)