from config import get_connection

class Connection:
    def __init__(self):
        self._connection = get_connection()

    def get(self):
        return self._connection

    def close(self):
        self._connection.close()
