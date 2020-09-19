from flask import Blueprint
from flask_restplus import Api

from app.main.controller.blogging_controller import api as home_api
from app.main.controller.user_controller import api as use_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Your Life in a Blog',
          version='1.0',
          description='blogging your life every day'
          )

api.add_namespace(home_api, '/home')
api.add_namespace(use_api, '/user')

