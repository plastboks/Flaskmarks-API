# api/views/mark.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort
from ..core.setup import Resource, auth, db
from ..core.validators import validate_email
from ..core.customfields import ApiKeyList
from ..models import User

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'created': fields.DateTime
}

class Profile(Resource):
    @auth.login_required
    @marshal_with(user_fields)
    def get(self):
        return g.user
