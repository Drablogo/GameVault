from database.base_repository import BaseRepository
from database.database import Database
from models import genre
from database.base_repository import BaseRepository


class GenreRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def add_genre(self, name: str):

        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO genres(name)
            VALUES (?)
            """,
            (name,)
        )

        connection.commit()

        self._close()

    def get_all_genres(self):

        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM genres
            ORDER BY name
            """
        )

        genre = cursor.fetchone()

        self._close()

        return genre

    def find_by_name(self, name: str):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name
            FROM genres
            WHERE name = ?
            """,
            (name,)
        )

        genre = cursor.fetchone()

        self._close()

        return genre

    def delete_genre(self, genre_id: int):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM genres
            WHERE id = ?
            """,
            (genre_id,)
        )

        connection.commit()

        self._close()