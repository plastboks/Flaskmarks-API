# api/views/mark.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort, marshal
from ..core.setup import Resource, auth, db


tag_fields = {
    'id': fields.Integer,
    'title': fields.String,
}


class Tags(Resource):
    @auth.login_required
    def get(self, page=1):
        tags = g.user.all_tags(page)
        return {'tags': marshal(tags.items, tag_fields),
                'pager': g.user.json_pager(tags)}
