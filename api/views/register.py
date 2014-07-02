# api/views/mark.py

from flask.ext.restful import reqparse
from ..core.setup import Resource, auth, db
from ..models import User


class Register(Resource):
    @auth.login_required
    def post(self, todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('email',
                            type=email,
                            required=True,
                            help='Missing email',
                            location='json')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='Missing password',
                            location='json') 
        args = parser.parse_args()
        u = User(args.email, args.password)
        try:
            db.session.add(u)
            db.session.commit()
            return {'status' : 'success'}, 200
        except Exception as detail:
            return {'status' : 'error'}, 400
