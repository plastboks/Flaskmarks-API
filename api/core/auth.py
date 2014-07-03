# api/core/auth.py

from flask import g
from .setup import auth
from ..models import User

@auth.verify_password
def verify_password(username, password):
    u = User.by_email(username)
    if not u or not u.verify_password(password):
        return False
    g.user = u
    return True
