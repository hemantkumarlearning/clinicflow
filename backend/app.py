# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from flask_cors import CORS

# JWT Manager
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)  # Enable if you're using a frontend

    # Register blueprints
    from routes import auth, users, doctors, appointments, patients
    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(doctors.bp)
    app.register_blueprint(appointments.bp)
    app.register_blueprint(patients.bp)

    @app.route('/')
    def index():
        return {"msg": "Clinic API is running"}

    return app

# For running locally
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
