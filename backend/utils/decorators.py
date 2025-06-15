# utils/decorators.py

from functools import wraps
from flask_jwt_extended import get_jwt_identity,get_jwt
from flask import jsonify

def role_required(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role")
            # identity = get_jwt_identity()
            if user_role not in allowed_roles:
                return jsonify({"msg": "Access denied: insufficient role"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
