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
core.setup.api.add_resource(views.Mark, '/mark/<string:todo_id>')
core.setup.api.add_resource(views.Marks, '/marks/<string:todo_id>')
