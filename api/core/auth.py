# api/core/auth.py

from flask import g, make_response, jsonify
from .setup import auth
from ..models import User


@auth.verify_password
def verify_password(username, password):
    u = User.by_email(username)
    if not u or not u.verify_password(password):
        return False
    g.user = u
    return True

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
