# api/views/mark.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse
from ..core.setup import Resource, auth, db
from ..models import Mark


mark_fields = {
    'id': fields.Integer,
    'type': fields.String,
    'title': fields.String,
    'url': fields.String,
    'clicks': fields.Integer,
    'last_clicked': fields.DateTime,
    'created': fields.DateTime,
    'updated': fields.DateTime
}

class Mark(Resource):
    @auth.login_required
    @marshal_with(mark_fields)
    def get(self, mark_id):
        mark = g.user.get_mark_by_id(mark_id) 
        if mark:
            return mark

    @auth.login_required
    @marshal_with(mark_fields)
    def post(self, mark_id):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str, required=True,
                            help='Missing type')
        parser.add_argument('title', type=str, required=True,
                            help='Missing title')
        parser.add_argument('url', type=str, required=True,
                            help='Missing url')
        parser.add_argument('tags', type=str)
        args = parser.parse_args()
        return g.user.create_mark(args.type,
                                  args.title,
                                  args.url,
                                  args.tags)


class Marks(Resource):
    @auth.login_required
    def get(self, page=1):
        marks = g.user.marks(page)
        return {'marks': marks.items,
                'pager': g.user.json_pager(marks)}
