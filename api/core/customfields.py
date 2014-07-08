# api/core/customfields

from flask.ext.restful import fields


class TagList(fields.Raw):
    def format(self, value):
        return [(t.title) for t in value]


class ApiKeyList(fields.Raw):
    def format(self, value):
        return [([t.app, t.value]) for t in value]
