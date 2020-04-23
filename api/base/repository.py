
class RepositoryException(Exception):
    pass



class BaseRepository():

    model = object

    db = object

    def __init__(self, Model, db):
        self.model = Model
        self.db = db

    def get(self):
        return self.model.query

    def filterBy(self, options):
        return self.model.query.filter_by(**options)

    def firstFilterBy(self, options):
        return self.filterBy(options).first()
    
    def getFilterBy(self, options):
        return self.filterBy(options).all()

    def countFilterBy(self, options):
        return self.filterBy(options).count()

    def insert(self, options):
        try:
            save =  self.model(**options)
            self.db.session.add(save)
            self.db.session.commit()
            return save
        except RepositoryException as e:
            self.db.session.rollback()
            raise RepositoryException("Insert failed error: {}".format(str(e)))

    def insertMany(self, optionsArray):
        try:
            manySave = []
            for options in optionsArray:
                save =  self.model(**options)
                manySave.append(save)
            self.db.session.add_all(manySave)
            self.db.session.commit()
            return manySave
        except RepositoryException as e:
            self.db.session.rollback()
            raise RepositoryException("insert many failed error: {}".format(str(e)))
    
    def deleteBy(self, options):
        try:
            self.filterBy(options).delete()
            self.db.session.commit()
        except RepositoryException as e:
            self.db.session.rollback()
            raise RepositoryException("Deleted failed error: {}".format(str(e)))


    def detelById(self, id):
        return self.deleteBy({"id": id})


    def updateBy(self, options, data):
        try:
            filterBy = self.filterBy(options).\
                update(data)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise RepositoryException("Failed update error:{} ".format(str(e)))
    

    def updateById(self, id, data):
        self.updateBy({'id': id}, data)
        

