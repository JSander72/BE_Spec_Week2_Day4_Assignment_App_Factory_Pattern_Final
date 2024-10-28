from app import create_app, db, ma
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

app = create_app('DevelopmentConfig')

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)