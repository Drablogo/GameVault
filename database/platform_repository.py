from database.database import Database
from database.base_repository import BaseRepository

class PlatformRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def add_platform(self, name: str):

        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO platforms(name)
            VALUES (?)
            """,
            (name,)
        )

        connection.commit()

        self._close()

    def get_all_platforms(self):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM platforms
            ORDER BY name
            """
        )

        platforms = cursor.fetchall()

        self._close()

        return platforms

    def delete_platform(self, platform_id: int):

        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM platforms
            WHERE id = ?
            """,
            (platform_id,)
        )

        connection.commit()

        self._close()

    def find_by_name(self, name: str):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM platforms
            WHERE name = ?
            """,
            (name,)
        )

        platform = cursor.fetchone()

        self._close()

        return platform