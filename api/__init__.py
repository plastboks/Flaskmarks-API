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
if core.setup.config['CAN_REGISTER']:
    core.setup.api.add_resource(views.Register, '/register')

core.setup.api.add_resource(views.Version, '/version')

core.setup.api.add_resource(views.Profile, '/profile')

core.setup.api.add_resource(views.Token, '/token', '/token/<string:key>')

core.setup.api.add_resource(views.Mark, '/mark', '/mark/<string:mark_id>')

core.setup.api.add_resource(views.Marks, '/marks', '/marks/<int:page>')

core.setup.api.add_resource(views.Tags, '/tags', '/tags/<int:page>')
