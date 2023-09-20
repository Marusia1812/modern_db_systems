import mysqlx
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = 'business'
DATA_DIR = os.path.join(PROJECT_DIR, 'data')

def get_connection():
    return mysqlx.get_session({
        'host': 'localhost',
        'port': 33060,
        'user': 'root',
        'password': 'Heslo123.'
    })

def get_collections(session: mysqlx.Session):
    schema = session.get_schema(DB_NAME)
    return {
        'bars': schema.get_collection('bars'),
        'clients': schema.get_collection('clients'),
        'addresses': schema.get_collection('addresses')
    }