from pymongo import MongoClient
from dataclasses import dataclass
import json
from pymongo.errors import PyMongoError, ConnectionFailure
from connect.connect_to_rpi import ConnectToMongoWithConfig

config_file = (
    "/home/giedrius/Documents/code_academy_projects/cafeteria/connect/config.json"
)
db = ConnectToMongoWithConfig.connect_to_mongodb(config=config_file)
