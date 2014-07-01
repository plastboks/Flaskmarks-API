# api/views/mark.py


from ..core.setup import Resource, auth


class Mark(Resource):
    @auth.login_required
    def get(self, todo_id):
        return {todo_id: "test"}


class Marks(Resource):
    @auth.login_required
    def get(self, todo_id):
        return {todo_id: "test"}
