# api/views/mark.py

from flask import g
from ..core.setup import Resource, auth, db
from ..models import Mark


class Mark(Resource):
    @auth.login_required
    def get(self, todo_id):
        return {todo_id: "test"}


class Marks(Resource):
    @auth.login_required
    def get(self, page=1):
        marks = g.user.marks(page)
        return {'marks': marks.items,
                'pager': g.user.json_pager(marks)}
