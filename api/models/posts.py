from . import db

class Posts(db.Model):
    __tablename__ = 'posts'
    # __table_args__ = {"schema": "example"}


    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title   = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    """ Time stamps """
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
