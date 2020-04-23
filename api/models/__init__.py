from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
"""
    add to register models 
"""
from .posts import Posts
from .users import Users

