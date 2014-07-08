# api/views/mark.py

from flask.ext.restful import fields, marshal_with, reqparse, abort
from ..core.setup import Resource, auth, db
from ..core.validators import validate_email
from ..core.customfields import ApiKeyList
from ..models import User

user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'created': fields.DateTime,
    'api_keys': ApiKeyList
}


def is_email(value):
    try:
        validate_email(value)
        return value
    except ValueError as e:
        raise ValueError(e)


class Register(Resource):
    @marshal_with(user_fields)
    def post(self):
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
