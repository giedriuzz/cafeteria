from pymongo import MongoClient
from pymongo.database import Database


class Connect:
    def connect_to_mongodb(self, host: str, port: int, db_name: str) -> Database:
        client = MongoClient(host, port)
        database = client[db_name]
        return database


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
