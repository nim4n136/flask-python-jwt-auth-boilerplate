from flask import Blueprint
from flask_restful import Api

# Controller
from api.v1.controllers import AuthLogin, AuthRegister, PostListController, PostController

blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(AuthRegister, '/auth/register')
api.add_resource(AuthLogin, '/auth/login')

api.add_resource(PostListController, '/posts')
api.add_resource(PostController, '/post/<id>')