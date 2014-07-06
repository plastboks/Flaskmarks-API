# api/views/mark.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort, marshal
from ..core.setup import Resource, auth, db
from ..core.customfields import TagList
from ..core.validators import validate_url
from ..models import Mark


mark_fields = {
    'id': fields.Integer,
    'type': fields.String,
    'title': fields.String,
    'url': fields.String,
    'tags': TagList,
    'clicks': fields.Integer,
    'last_clicked': fields.DateTime,
    'created': fields.DateTime,
    'updated': fields.DateTime
}


def is_url(value):
    try:
        validate_url(value)
        return value
    except ValueError as e:
        raise ValueError(e)


class Mark(Resource):
    @auth.login_required
    @marshal_with(mark_fields)
    def get(self, mark_id):
        mark = g.user.get_mark_by_id(mark_id)
        if mark:
            return mark
        return abort(410, message="Mark {} doesn't exist".format(mark_id))

    @auth.login_required
    @marshal_with(mark_fields)
    def put(self, mark_id):
        put_parser = reqparse.RequestParser()
        put_parser.add_argument('type', type=str)
        put_parser.add_argument('title', type=str)
        put_parser.add_argument('url', type=str)
        put_parser.add_argument('tags', type=str)
        args = put_parser.parse_args()
        mark = g.user.get_mark_by_id(mark_id)
        if mark:
            return mark.update_mark(args)
        return abort(410, message="Mark {} doesn't exist".format(mark_id))

    @auth.login_required
    @marshal_with(mark_fields)
    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument('type', type=str, required=True,
                                 help='Missing type')
        post_parser.add_argument('title', type=str, required=True,
                                 help='Missing title')
        post_parser.add_argument('url', type=is_url, required=True)
        post_parser.add_argument('tags', type=str)
        args = post_parser.parse_args()
        return g.user.create_mark(args.type,
                                  args.title,
                                  args.url,
                                  args.tags)


class Marks(Resource):
    @auth.login_required
    def get(self, page=1):
        get_parser = reqparse.RequestParser()
        get_parser.add_argument('q', type=str)
        get_parser.add_argument('tag', type=str)
        get_parser.add_argument('type', type=str)
        get_parser.add_argument('sort', type=str)
        args = get_parser.parse_args()
        marks = g.user.marks(page,
                             q=args.q,
                             type=args.type,
                             tag=args.tag,
                             sort=args.sort)
        return {'marks': marshal(marks.items, mark_fields),
                'pager': g.user.json_pager(marks)}
