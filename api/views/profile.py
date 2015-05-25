# api/views/profile.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse
from ..core.setup import Resource, auth
from register import is_email

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'per_page': fields.Integer,
    'email': fields.String,
    'created': fields.DateTime
}


class Profile(Resource):
    @auth.login_required
    @marshal_with(user_fields)
    def get(self):
        return g.user

    @auth.login_required
    @marshal_with(user_fields)
    def put(self):
        put_parser = reqparse.RequestParser()
        put_parser.add_argument('username', type=str)
        put_parser.add_argument('email', type=is_email)
        put_parser.add_argument('password', type=is_email)
        put_parser.add_argument('per_page', type=int)

        args = put_parser.parse_args()
        return g.user.update(args)

    @auth.login_required
    @marshal_with(user_fields)
    def delete(self):
        return g.user.delete()
