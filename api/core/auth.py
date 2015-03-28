# api/core/auth.py

from flask import g, make_response, jsonify
from flask.ext.restful import abort
from .setup import auth
from ..models import User


@auth.verify_password
def verify_password(username_or_token, password):
    u = User.verify_api_key(username_or_token)
    if not u:
        u = User.by_email(username_or_token)
        if not u or not u.verify_password(password):
            return False
    g.user = u
    return True

@auth.error_handler
def unauthorized():
    return abort(401, message="Unauthorized access")
