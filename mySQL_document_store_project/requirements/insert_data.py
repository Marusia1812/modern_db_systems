import json
from connection import Connection
from config import DATA_DIR

def insert_data(collections, connection: Connection):
    for collection in collections:
        with open(f'{DATA_DIR}/{collection}.json') as f:
            data = json.load(f)
            for doc in data:
                collections[collection].add(doc).execute()
