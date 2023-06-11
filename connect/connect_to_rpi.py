from pymongo import MongoClient
from dataclasses import dataclass
import json
from pymongo.errors import PyMongoError, ConnectionFailure


@dataclass
class MainRpiRemoteDb:
    user_name: str
    user_passwd: str
    host: str
    port: int
    db_name: int


class ConnectToMongoWithConfig:
    def connect_to_mongodb(config: str) -> MongoClient:
        """prisijungiama prie RPI"""
        try:
            with open(config, "r") as f:
                config = json.load(f)

            host = config.get("host")
            port = config.get("port")
            username = config.get("user_name")
            password = config.get("user_psswd")
            auth_source = config.get("database")

            db = MainRpiRemoteDb(
                user_name=username,
                user_passwd=password,
                host=host,
                port=port,
                db_name=auth_source,
            )
            return db

        except ConnectionFailure as e:
            print("Connection failure:", str(e))
            return None
        except PyMongoError as e:
            print("An error occurred:", str(e))
            return None


if __name__ == "__main__":
    pass
