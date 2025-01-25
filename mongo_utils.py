from pymongo import MongoClient

def get_mongo_collection(
    uri="mongodb://localhost:27017",
    db_name="crawler_db",
    collection_name="pages"
):
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

def store_in_mongo(collection, document):
    try:
        collection.insert_one(document)
        print(f"stored URL page: {document['url']}")
    except Exception as e:
        print(f"Failed to store document: {e}")
