from datetime import datetime
from distutils.log import error
import sys
from typing import Set, List, Dict
from pymongo.errors import DuplicateKeyError

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
            home_dict = home.__dict__
            home_dict["created_at"] = datetime.utcnow().isoformat()
            home_dict["updated_at"] = datetime.utcnow().isoformat()

            homes_parsed.append(home_dict)
        return homes_parsed
    
    def save(self, homes: Set[Home]) -> None:
        homes_parsed = self.parse_homes(homes)

        for home in homes_parsed:
            try:
                self.collection.insert_one(home)
            except DuplicateKeyError:
                self.collection.find_one_and_update(
                    {
                        "link": home["link"]
                    },
                    {
                        "$set":
                        {
                            "updated_at": datetime.utcnow().isoformat()
                        }
                    }
                )
            except:
                print("unexepected error occurs")
                sys.exit()
