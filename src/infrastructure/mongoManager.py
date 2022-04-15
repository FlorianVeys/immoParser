from pymongo import MongoClient
from infrastructure.config import MONGO_DB


class MongoManager(object):
    __database = None

    @staticmethod
    def getDatabase():
        if MongoManager.__database == None:
            MongoManager()
        return MongoManager.__database

    def __init__(self):
        if MongoManager.__database != None:
            raise Exception("This class is a singleton!")
        else:
            MongoManager.__database = MongoClient(MONGO_DB.URL, MONGO_DB.PORT)[MONGO_DB.DATABASE]
