from api.base import BaseRepository
from api.models import Posts, db

class PostsRepository(BaseRepository):
    
    def __init__(self):
       BaseRepository.__init__(self, Model=Posts, db=db) 
