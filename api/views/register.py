# api/views/mark.py

from flask.ext.restful import reqparse
from ..core.setup import Resource, auth, db
from ..models import User


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email',
                            type=str,
                            required=True,
                            help='Missing email'
                            )
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='Missing password'
                            ) 
        args = parser.parse_args()
        u = User(args.email, args.password)
        try:
            db.session.add(u)
            db.session.commit()
            return {'message' : 'User created'}, 201
        except Exception as detail:
            return {'message' : 'User exists'}, 409
