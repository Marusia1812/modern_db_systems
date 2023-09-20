from connection import Connection
from config import DB_NAME

def drop_schema(connection: Connection, schema_name: str):
    session = connection.get()
    if schema_name in session.get_schemas():
        session.drop_schema(schema_name)

def create_schema_and_collections(connection: Connection):
    drop_schema(connection, DB_NAME)

    session = connection.get()
    schema = session.create_schema(DB_NAME)

    collections = {
        'bars': schema.create_collection('bars'),
        'clients': schema.create_collection('clients'),
        'addresses': schema.create_collection('addresses')
    }

    return collections
