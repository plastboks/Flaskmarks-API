# api/views/mark.py


from ..core.setup import Resource


class Mark(Resource):
    def get(self, todo_id):
        return {todo_id: "test"}


class Marks(Resource):
    def get(self, todo_id):
        return {todo_id: "test"}
