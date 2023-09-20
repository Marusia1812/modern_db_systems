mimport time
from connection import Connection
from create_schema import create_schema_and_collections
from insert_data import insert_data
from queries import (bars_query, clients_query, addresses_query,
                     founded_after_with_wifi_and_smokeasies, clients_older_than_30_visited_br1)
from measure_time import measure_avg_time

if __name__ == "__main__":
    # Creating a schema and collections
    connection = Connection()
    collections = create_schema_and_collections(connection)
    
    # Inserting documents into a collection
    insert_data(collections, connection)
    
    # Queries
    barsQuery = bars_query(collections, connection).execute().fetch_all()
    clientsQuery = clients_query(collections, connection).execute().fetch_all()
    addressesQuery = addresses_query(collections, connection).execute().fetch_all()
    complexQuery1 = founded_after_with_wifi_and_smokeasies(collections, connection).execute().fetch_all()
    complexQuery2 = clients_older_than_30_visited_br1(collections, connection).execute().fetch_all()

    # Print results
    print('Query 1. Get all bars:')
    for doc in barsQuery:
        print(doc)
    print('Query 2. Get first two clients:')
    for doc in clientsQuery:
        print(doc)
    print('Query 3. Get second address:')
    for doc in addressesQuery:
        print(doc)
    print('Query 4. Get bars founded after 2010 with wifi and smokeasies:')
    for doc in complexQuery1:
        print(doc)
    print('Query 5. Get clients older than 30 who visited bar br1:')
    for doc in complexQuery2:
        print(doc)

    # Measure time of queries
    print('Time of previous queries:')
    print(f'Query 1: {measure_avg_time(10, bars_query, collections, connection)}')
    print(f'Query 2: {measure_avg_time(10, clients_query, collections, connection)}')
    print(f'Query 3: {measure_avg_time(10, addresses_query, collections, connection)}')
    print(f'Query 4: {measure_avg_time(10, founded_after_with_wifi_and_smokeasies, collections, connection)}')
    print(f'Query 5: {measure_avg_time(10, clients_older_than_30_visited_br1, collections, connection)}')

    # Close connection
    connection.close()