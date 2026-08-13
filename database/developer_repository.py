from database.database import Database
from database.base_repository import BaseRepository

class DeveloperRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def add_developer(self, name: str):

        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO developers(name)
            VALUES (?)
            """,
            (name,)
        )

        connection.commit()

        self._close()

    def get_all_developers(self):

        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM developers
            ORDER BY name
            """
        )

        developers = cursor.fetchall()

        self._close()

        return developers

    def find_by_name(self, name: str):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM developers
            WHERE name = ?
            """,
            (name,)
        )

        developers = cursor.fetchone()

        self._close()

        return developers

    def delete_developer(self, developer_id: int):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM developers
            WHERE id = ?
            """,
            (developer_id,)
        )

        connection.commit()
        self._close()