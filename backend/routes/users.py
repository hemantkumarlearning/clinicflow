# routes/users.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Doctor
from utils.decorators import role_required

bp = Blueprint('users', __name__)

@bp.route('/users/doctor', methods=['POST'])
@jwt_required()
@role_required('admin')
def create_doctor():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    specialty = data.get('specialty')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 409

    hashed_pw = generate_password_hash(password)
    user = User(username=username, password=hashed_pw, role='doctor')
    db.session.add(user)
    db.session.commit()

    doctor = Doctor(user_id=user.id, name=name, specialty=specialty)
    db.session.add(doctor)
    db.session.commit()

    return jsonify({"msg": "Doctor account created successfully"}), 201

@bp.route('/users/receptionist', methods=['POST'])
@jwt_required()
@role_required('admin')
def create_receptionist():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 409

    hashed_pw = generate_password_hash(password)
    user = User(username=username, password=hashed_pw, role='receptionist')
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Receptionist account created successfully"}), 201

@bp.route('/users', methods=['GET'])
@jwt_required()
@role_required('admin')
def list_users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "role": u.role
        } for u in users
    ])
