# api/core/auth.py

from flask import g
from ..models import User

@auth.verify_password
def verify_password(username, password):
    user = User.by_email(username, password)
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True
