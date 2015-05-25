# api/views/setting.py

from flask import g
from flask.ext.restful import fields, marshal_with, reqparse, abort
from ..core.setup import Resource, auth
import json


setting_fields = {
    'name': fields.String,
    'json': fields.String,
    'created': fields.DateTime,
    'updated': fields.DateTime
}


def is_json(value):
    try:
        json.dumps(value)
        return value
    except SyntaxError:
        raise "Invalid JSON format"


class Setting(Resource):
    @auth.login_required
    @marshal_with(setting_fields)
    def get(self, name):
        setting = g.user.get_setting_by_name(name)
        if setting:
            return setting
        return abort(410, message="Setting {} doesn't exists".format(name))

    @auth.login_required
    @marshal_with(setting_fields)
    def put(self, name):
        put_parser = reqparse.RequestParser()
        put_parser.add_argument('json', type=is_json, required=True,
                                help='Missing JSON setting blob')
        args = put_parser.parse_args()
        setting = g.user.get_setting_by_name(name)
        if setting:
            return setting.update(args)
        return abort(410, message="Setting {} doesn't exist".format(name))

    @auth.login_required
    @marshal_with(setting_fields)
    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument('name', type=str, required=True,
                                 help='Missing name')
        post_parser.add_argument('json', type=is_json, required=True,
                                 help='Missing JSON setting blob')
        args = post_parser.parse_args()
        return g.user.create_setting(args.name, args.json)

    @auth.login_required
    @marshal_with(setting_fields)
    def delete(self, name):
        setting = g.user.get_setting_by_name(name)
        if setting:
            setting.delete()
            return setting
        return abort(410, message="Setting {} doesn't exist".format(name))
