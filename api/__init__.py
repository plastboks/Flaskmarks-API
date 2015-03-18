# @package Flaskmarks API
#
# @version 0.01
#
# @author Alexander Skjolden
#
# @date 2014-06-30
#


from flask import Flask
app = Flask(__name__, instance_relative_config=True)

from . import core
from . import models
from . import views

# routes
core.setup.api.add_resource(views.Register, '/register')

core.setup.api.add_resource(views.Token,
                            '/token', '/token/<string:key>',
                            endpoint='token')
core.setup.api.add_resource(views.Tokens,
                            '/tokens', '/tokens/<int:page>',
                            endpoint='tokens')

core.setup.api.add_resource(views.Mark,
                            '/mark', '/mark/<string:mark_id>',
                            endpoint='mark')
core.setup.api.add_resource(views.Marks,
                            '/marks', '/marks/<int:page>',
                            endpoint='marks')

core.setup.api.add_resource(views.Tags,
                            '/tags', '/tags/<int:page>',
                            endpoint='tags')
