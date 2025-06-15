# routes/doctors.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import Doctor

bp = Blueprint('doctors', __name__)

@bp.route('/doctors', methods=['GET'])
@jwt_required()
def list_doctors():
    # specialty = request.args.get('specialty')
    # query = Doctor.query

    # if specialty:
    #     query = query.filter(Doctor.specialty.ilike(f'%{specialty}%'))

    # doctors = query.all()

    # return jsonify([
    #     {
    #         "id": d.id,
    #         "name": d.name,
    #         "specialty": d.specialty
    #     } for d in doctors
    # ])
    doctors = Doctor.query.all()
    result = [{
        "id": doc.id,
        "name": doc.name,
        "specialty": doc.specialty
    } for doc in doctors]

    return jsonify({"doctors": result}), 200