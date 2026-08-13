from models.game import Game
from models.platform import Platform
from models.genre import Genre
from models.developer import Developer
from models.game_state import GameState


class GameMapper:

    @staticmethod
    def to_game(row):

        if row is None:
            return None

        return Game(
            game_id=row[0],
            title=row[1],
            release_year=row[2],

            platform=Platform(
                platform_id=row[3],
                name=row[4]
            ),

            genre=Genre(
                genre_id=row[5],
                name=row[6]
            ),

            developer=Developer(
                developer_id=row[7],
                name=row[8]
            ),

            state=GameState(row[9]),
            playtime=row[10],
            rating=row[11],
            cover_path=row[12]
        )