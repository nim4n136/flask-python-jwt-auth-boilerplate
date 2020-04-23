from . import db

class Users(db.Model):
    __tablename__ = 'users'
    # __table_args__ = {"schema": "example"}

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(255), nullable=False)
    username    = db.Column(db.String(255), unique=True, nullable=False)
    email       = db.Column(db.String(255), unique=True, nullable=False)
    password    = db.Column(db.String(255), nullable=False)


    """ Time stamps """
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())