# api/views/mark.py

from ..core.setup import Resource, auth, db, config

class Version(Resource):
    def get(self):
        return {'version': config['version'].strip()}
