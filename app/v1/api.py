from flask import Blueprint
from flask_restful import Api

# Controller
from app.v1.controllers.auth import AuthLogin, AuthRegister
from app.v1.controllers.user import User

blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(AuthRegister, '/auth/register')
api.add_resource(AuthLogin, '/auth/login')
api.add_resource(User, '/user')
