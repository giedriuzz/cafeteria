from pymongo import MongoClient
<<<<<<< HEAD
from dataclasses import dataclass
from pymongo.database import Database


class Connect:  # Leaved if use a docker on compatible machine without user authentication
=======
from pymongo.database import Database


class Connect:
>>>>>>> 08e552542a7b094f59b64ba9ec27b9ba4498b81b
    def connect_to_mongodb(self, host: str, port: int, db_name: str) -> Database:
        client = MongoClient(host, port)
        database = client[db_name]
        return database


<<<<<<< HEAD
@dataclass
class ConnectToRpi4:
    user_name: str
    user_passwd: str
    host: str
    port: int
    db_name: int
    collection_name: str


if __name__ == "__main__":
    pass
=======
# Example usage
if __name__ == "__main__":
    connect = Connect()
    # # Connection details
    # mongodb_host = "localhost"
    # mongodb_port = 27017
    # database_name = "mydatabase"

    # # Connect to MongoDB
    # db = connect.connect_to_mongodb(mongodb_host, mongodb_port, database_name)
    # print(
    #     f"Connected to MongoDB: {mongodb_host}:{mongodb_port}, Database: {database_name}"
    # )
>>>>>>> 08e552542a7b094f59b64ba9ec27b9ba4498b81b
