from api.base import BaseRepository
from api.models import Users, db

class UsersRepository(BaseRepository):
    
    def __init__(self):
       BaseRepository.__init__(self, Model=Users, db=db) 
