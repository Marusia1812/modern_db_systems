def bars_query(collections, connection):
    return collections['bars'].find()

def clients_query(collections, connection):
    return collections['clients'].find().limit(2)

def addresses_query(collections, connection):
    return collections['addresses'].find().offset(1).limit(1)

def founded_after_with_wifi_and_smokeasies(collections, connection):
    query = "founded > :founded AND wifi = :wifi AND terrace.smokeasies = :smokeasies"
    return collections['bars'].find(query)\
        .bind("founded", '2010-01-01')\
        .bind("wifi", True)\
        .bind("smokeasies", True)

def clients_older_than_30_visited_br1(collections, connection):
    query = "age > :age AND JSON_CONTAINS(visited, :bar_id)"
    return collections['clients'].find(query).fields("givenName")\
        .bind("age", 30)\
        .bind("bar_id", '\"br1\"')\
        .limit(3)
