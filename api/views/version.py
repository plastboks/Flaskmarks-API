# api/views/version.py

from ..core.setup import Resource, config


class Version(Resource):
    def get(self):
        return {'version': config['version'].strip()}
