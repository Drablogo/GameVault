import sqlite3

class Database:
    def __init__(self, db_name="database.db"):
        self._db_name = db_name
        self._connection = None

    def connect(self):
        self._connection = sqlite3.connect(self._db_name)
        return self._connection

    def close(self):
        if self._connection:
            self._connection.close()