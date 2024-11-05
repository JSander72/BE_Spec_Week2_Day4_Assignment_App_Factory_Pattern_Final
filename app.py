from app import create_app
from app.models import db
from flask import current_app

app = create_app('DevelopmentConfig')

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()

    with app.app_context():
        # Your code that uses current_app.extensions['limiter'].limit("10 per hour")
        pass

    app.run(debug=True)