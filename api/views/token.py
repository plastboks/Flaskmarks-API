# api/views/mark.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort, marshal
from ..core.setup import Resource, auth, db
from ..core.customfields import TagList
from ..core.validators import validate_url
from ..models import Mark


token_fields = {
    'key': fields.String,
    'value': fields.String
}

class Token(Resource):
    @auth.login_required
    @marshal_with(token_fields)
    def get(self, key):
        token = g.user.get_token_by_key(key)
        if token:
            return token
        return abort(410, message="Unknown {} token key".format(key))

    @auth.login_required
    @marshal_with(token_fields)
    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument('key', type=str, required=True,
                                 help='Missing key')
        args = post_parser.parse_args()
        return g.user.new_apikey(args.key)



class Tokens(Resource):
    @auth.login_required
    def get(self, page=1):
        tokens = g.user.tokens(page)
        return {'tokens': marshal(tokens.items, token_fields),
                'pager': g.user.json_pager(tokens)}
