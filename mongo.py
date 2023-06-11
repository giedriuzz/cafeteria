from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List


class MongoDb:
    # Create(Insert)
    def insert_create_document(self, collection: Collection, document: Dict) -> str:
        result = collection.insert_one(document)
        return str(result.inserted_id)

    # Read
    def find_documents(self, collection: Collection, query: Dict) -> List[Dict]:
        documents = collection.find(query)
        return list(documents)

    # Update
    def update_document(self, collection: Collection, query: Dict, update: Dict) -> int:
        result = collection.update_many(query, {"$set": update})
        return result.modified_count

    # Delete
    def delete_documents(self, collection: Collection, query: Dict) -> int:
        result = collection.delete_many(query)
        return result.deleted_count

    def get_database_collection(
        self, database: Database, collection_name: str
    ) -> Collection:
        collection = database[collection_name]
        return collection

    def list_databases(self, client: MongoClient) -> List[str]:
        return client.list_database_names()

    def list_collections(self, database: Database) -> List[str]:
        return database.list_collection_names()
