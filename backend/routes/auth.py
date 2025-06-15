# routes/auth.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import db, User, Patient
from datetime import datetime

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    dob = data.get('dob')  # Format: YYYY-MM-DD
    gender = data.get('gender')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 409

    hashed_pw = generate_password_hash(password)
    user = User(username=username, password=hashed_pw, role='patient')
    db.session.add(user)
    db.session.commit()

    patient = Patient(
        user_id=user.id,
        name=name,
        dob=datetime.strptime(dob, "%Y-%m-%d").date(),
        gender=gender
    )
    db.session.add(patient)
    db.session.commit()

    return jsonify({"msg": "Patient registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid username or password"}), 401

    access_token = create_access_token(
    identity=str(user.id),  # or just user.id if it's already a string
    additional_claims={"role": user.role}
    )
    return jsonify({
    "access_token": access_token,
    "role": user.role
}), 200
