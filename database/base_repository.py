from database.database import Database


class BaseRepository:

    def __init__(self):
        self._database = Database()

    def _connect(self):
        return self._database.connect()

    def _close(self):
        self._database.close()