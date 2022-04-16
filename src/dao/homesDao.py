from typing import Set, List, Dict

from infrastructure.mongoManager import MongoManager
from model.home import Home

class HomesDao:
    unique_index_on = "link"

    def __init__(self):
        self.collection = MongoManager.getDatabase()['homes']
        self.collection.create_index(self.unique_index_on, unique=True)

    def parse_homes(self, homes: Set[Home]) -> List[Dict]:
        homes_parsed = []
        for home in homes:
            homes_parsed.append(home.__dict__)
        return homes_parsed
    
    def save(self, homes: Set[Home]) -> None:
        self.collection.insert_many(self.parse_homes(homes))
