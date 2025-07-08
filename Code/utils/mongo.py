from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Any, Dict, List, Optional


class MongoDBInterface:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection: Collection = self.db[collection_name]

    def create_document(self, data: Dict[str, Any]) -> str:
        """Insert a new document into the collection."""
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def read_documents(self, query: Dict[str, Any] = {}, projection: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Find documents matching the query."""
        return list(self.collection.find(query, projection))

    def read_document_by_id(self, document_id: Any) -> Optional[Dict[str, Any]]:
        """Find a single document by its _id."""
        return self.collection.find_one({"_id": document_id})

    def update_document(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        """Update documents matching the query."""
        result = self.collection.update_many(query, {"$set": update_data})
        return result.modified_count

    def delete_document(self, query: Dict[str, Any]) -> int:
        """Delete documents matching the query."""
        result = self.collection.delete_many(query)
        return result.deleted_count

    def close_connection(self):
        """Close the MongoDB client connection."""
        self.client.close()

    def get_max_value(self, field: str, query: Dict[str, Any] = {}) -> Any:
        """Retrieve the highest value of a specific field in the collection. Defaults to 1 if none found."""
        result = self.collection.find(query, {field: 1, "_id": 0}).sort(field, -1).limit(1)
        doc = next(result, None)
        return doc.get(field) if doc and field in doc else 0
