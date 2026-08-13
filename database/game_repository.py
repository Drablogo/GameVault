from database.database import Database
from database.game_mapper import GameMapper
from database.base_repository import BaseRepository

class GameRepository(BaseRepository):

    def __init__(self):
        super().__init__()

    def add_game(self, game):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO games
            (
                title,
                release_year,
                platform_id,
                genre_id,
                developer_id,
                state,
                playtime,
                rating,
                cover_path
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                game.title,
                game.release_year,
                game.platform.id,
                game.genre.id,
                game.developer.id,
                game.state.value,
                game.playtime,
                game.rating,
                game.cover_path
            )
        )

        connection.commit()

        self._close()

    def get_all_games(self):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                games.id,
                games.title,
                games.release_year,
            
                platforms.id,
                platforms.name,
            
                genres.id,
                genres.name,
            
                developers.id,
                developers.name,
            
                games.state,
                games.playtime,
                games.rating,
                games.cover_path
            
            FROM games
            
            JOIN platforms
                ON games.platform_id = platforms.id
                
            JOIN genres
                ON games.genre_id = genres.id
                
            JOIN developers
                ON games.developer_id = developers.id
                
            ORDER BY games.title
        """)

        rows = cursor.fetchall()

        self._close()

        return [GameMapper.to_game(row) for row in rows]

    def get_game_by_id(self, game_id):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                games.id,
                games.title,
                games.release_year,
            
                platforms.id,
                platforms.name,
            
                genres.id,
                genres.name,
            
                developers.id,
                developers.name,
            
                games.state,
                games.playtime,
                games.rating,
                games.cover_path

            FROM games

            JOIN platforms
                ON games.platform_id = platforms.id

            JOIN genres
                ON games.genre_id = genres.id

            JOIN developers
                ON games.developer_id = developers.id

            WHERE games.id = ?
            """,
            (game_id,)
        )

        row = cursor.fetchone()

        self._close()

        return GameMapper.to_game(row)

    def update_game(self, game):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE games
            SET
                title = ?,
                release_year = ?,
                platform_id = ?,
                genre_id = ?,
                developer_id = ?,
                state = ?,
                playtime = ?,
                rating = ?,
                cover_path = ?
            WHERE id = ?
            """,
            (
                game.title,
                game.release_year,
                game.platform.id,
                game.genre.id,
                game.developer.id,
                game.state.value,
                game.playtime,
                game.rating,
                game.cover_path,
                game.id
            )
        )

        connection.commit()

        self._close()

    def delete_game(self, game_id):
        connection = self._connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM games
            WHERE id = ?
            """,
            (game_id,)
        )

        connection.commit()

        self._close()

    def find_by_title(self, title: str):
        connection = self._database.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM games
            WHERE title = ?
            """,
            (title,)
        )

        game = cursor.fetchone()

        self._database.close()

        return game
