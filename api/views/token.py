# api/views/mark.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort, marshal
from ..core.setup import Resource, auth, db
from ..core.customfields import TagList
from ..core.validators import validate_url
from ..models import Mark


token_fields = {
    'key': fields.String,
    'expires': fields.DateTime,
    'unhashed': fields.String
}


class Token(Resource):
    @auth.login_required
    @marshal_with(token_fields)
    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument('key', type=str, required=True,
                                 help='Missing key')
        args = post_parser.parse_args()
        return g.user.create_apikey(args.key)
