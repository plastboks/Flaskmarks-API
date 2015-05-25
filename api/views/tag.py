# api/views/tag.py

from flask import g
from flask.ext.restful import fields, marshal
from ..core.setup import Resource, auth


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
