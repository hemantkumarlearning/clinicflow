
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Appointment, Patient, Doctor
from utils.decorators import role_required
from datetime import datetime

bp = Blueprint('appointments', __name__)

# --------------------------
# 1. PATIENT: Book Appointment
# --------------------------
@bp.route('/appointments', methods=['POST'])
@jwt_required()
@role_required('patient')
def book_appointment():
    user_id = get_jwt_identity()
    # user_id = identity["id"]

    data = request.get_json()
    doctor_id = data.get('doctor_id')
    doctor_name = data.get('doctor_name')
    date_str = data.get('date')
    reason = data.get('reason')

    date_obj = datetime.fromisoformat(date_str)

    patient = Patient.query.filter_by(user_id=user_id).first()
    if not patient:
        return jsonify({"msg": "Patient profile not found"}), 404

    appointment = Appointment(
        patient_id=patient.id,
        doctor_id=doctor_id,
        doctor_name=doctor_name,
        date=date_obj,
        reason=reason,
        status='pending'
    )

    db.session.add(appointment)
    db.session.commit()

    return jsonify({
        "msg": "Appointment booked successfully",
        "appointment_id": appointment.id,
        "status": appointment.status
    }), 201

# --------------------------
# 2. RECEPTIONIST: View Pending
# --------------------------
@bp.route('/appointments/pending', methods=['GET'])
@jwt_required()
@role_required('receptionist')
def view_pending():
    appointments = Appointment.query.filter_by(status='pending').all()
    return jsonify([
        {
            "id": a.id,
            "patient_id": a.patient_id,
            "doctor_id": a.doctor_id,
            "date": a.date.isoformat(),
            "reason": a.reason
        } for a in appointments
    ])

# --------------------------
# 3. RECEPTIONIST: Confirm Appointment
# --------------------------
@bp.route('/appointments/<int:id>/confirm', methods=['PATCH'])
@jwt_required()
@role_required('receptionist')
def confirm_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    appointment.status = 'confirmed'
    db.session.commit()
    return jsonify({"msg": "Appointment confirmed"})

# --------------------------
# 4. PATIENT: View Own Appointments
# --------------------------
@bp.route('/appointments/patient', methods=['GET'])
@jwt_required()
@role_required('patient')
def patient_appointments():
    user_id = get_jwt_identity()
    patient = Patient.query.filter_by(user_id=user_id).first()
    if not patient:
        return jsonify({"msg": "Patient profile not found"}), 404

    appointments = Appointment.query.filter_by(patient_id=patient.id).all()
    return jsonify([
        {
            "id": a.id,
            "doctor_id": a.doctor_id,
            "doctor_name": a.doctor_name,
            "date": a.date.isoformat(),
            "reason": a.reason,
            "status": a.status
        } for a in appointments
    ])

# --------------------------
# 5. DOCTOR: View Own Appointments
# --------------------------
@bp.route('/appointments/doctor', methods=['GET'])
@jwt_required()
@role_required('doctor')
def doctor_appointments():
    user_id = get_jwt_identity()
    doctor = Doctor.query.filter_by(user_id=user_id).first()
    if not doctor:
        return jsonify({"msg": "Doctor profile not found"}), 404

    appointments = Appointment.query.filter_by(doctor_id=doctor.id).all()
    return jsonify([
        {
            "id": a.id,
            "patient_id": a.patient_id,
            "date": a.date.isoformat(),
            "reason": a.reason,
            "status": a.status
        } for a in appointments
    ])

# --------------------------
# 6. ADMIN: View All Appointments
# --------------------------
@bp.route('/appointments', methods=['GET'])
@jwt_required()
@role_required('admin')
def all_appointments():
    appointments = Appointment.query.all()
    return jsonify([
        {
            "id": a.id,
            "patient_id": a.patient_id,
            "doctor_id": a.doctor_id,
            "date": a.date.isoformat(),
            "reason": a.reason,
            "status": a.status
        } for a in appointments
    ])

# --------------------------
# 7. ADMIN: Delete Appointment
# --------------------------
@bp.route('/appointments/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    return jsonify({"msg": "Appointment deleted"})
