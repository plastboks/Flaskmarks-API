# @package Flaskmarks API
#
# @version 0.01
#
# @author Alexander Skjolden
#
# @date 2014-06-30
#


from flask import Flask
app = Flask(__name__)

from . import core
from . import models
from . import views

# routes
core.setup.api.add_resource(views.Register, '/register')

core.setup.api.add_resource(views.Mark,
                            '/mark', '/mark/<string:mark_id>',
                            endpoint='mark')
core.setup.api.add_resource(views.Marks, '/marks/default/<int:page>')
