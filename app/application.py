"""
application.py
- creates a Flask app instance and registers the database object
"""
from flask import Flask
from flask_cors import CORS
from .v1.api import blueprint as api_v1

def create_app(app_name='NETWORK_REPORTING'):

  app = Flask(app_name)

  app.config.from_object('app.config.BaseConfig')

  CORS(app, resources={r"/api/*": {"origins": "*"}})

  app.register_blueprint(api_v1)

  return app