import time
from connection import Connection

def measure_avg_time(count: int, query_function, collections: dict, connection: Connection):
    total_time = 0
    
    for _ in range(count):
        start_time = time.time()
        result = query_function(collections, connection).execute().fetch_all()
        end_time = time.time()
        
        total_time += (end_time - start_time)
    
    return total_time / count
