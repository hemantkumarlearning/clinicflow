# routes/patients.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import Patient, User
from utils.decorators import role_required
from models import db

bp = Blueprint('patients', __name__)

# --------------------------
# 1. ADMIN: View All Patients
# --------------------------
@bp.route('/patients', methods=['GET'])
@jwt_required()
@role_required('admin')
def get_all_patients():
    patients = Patient.query.all()
    return jsonify([
        {
            "id": p.id,
            "user_id": p.user_id,
            "name": p.name,
            "dob": p.dob.isoformat(),
            "gender": p.gender,
            "username": p.user.username
        } for p in patients
    ])

# --------------------------
# 2. ADMIN: Delete Patient
# --------------------------
@bp.route('/patients/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    user = User.query.get(patient.user_id)

    db.session.delete(patient)
    if user:
        db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "Patient and user deleted successfully"}), 200
