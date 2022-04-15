from infrastructure.mongoManager import MongoManager

class HomesDao:
    def __init__(self):
        self.collection = MongoManager.getDatabase()['homes']

    def save(self, homes):
        # TODO - save in mongo
        # self.collection.insert_many(
        #     map(
        #         lambda home: home.dump(),
        #         homes
        #     )
        # )

        None