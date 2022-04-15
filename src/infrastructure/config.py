import os
from dotenv import load_dotenv

load_dotenv()

class MONGO_DB:
    URL = os.environ.get("MONGO_DB_URL")
    PORT = os.environ.get("MONGO_DB_PORT")
    DATABASE = os.environ.get("MONGO_DB_DATABASE")
