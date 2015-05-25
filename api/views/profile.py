# api/views/profile.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort
from ..core.setup import Resource, auth, config
from ..models import User
from ..core.validators import validate_email

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'per_page': fields.Integer,
    'email': fields.String,
    'created': fields.DateTime
}


def is_email(value):
    try:
        validate_email(value)
        return value
    except ValueError as e:
        raise ValueError(e)


class Profile(Resource):
    @marshal_with(user_fields)
    def post(self):
        if not config['CAN_REGISTER']:
            return abort(405, message="User registration is disabled")

        post_parser = reqparse.RequestParser()
        post_parser.add_argument('email',
                                 type=is_email,
                                 required=True
                                 )
        post_parser.add_argument('password',
                                 type=str,
                                 required=True,
                                 help='Missing password'
                                 )
        args = post_parser.parse_args()
        u = User(args.email, args.password)
        user = u.save()
        if user:
            return user
        return abort(409, message="User with this email {} exists"
                     .format(args.email))

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
