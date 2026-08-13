from services.game_service import GameService

from models.game import Game
from models.platform import Platform
from models.genre import Genre
from models.developer import Developer
from models.game_state import GameState


class Seed:

    def __init__(self):
        self._service = GameService()

    def _add_if_not_exists(self, game: Game):

        if self._service.game_exists(game.title):
            return

        self._service.add_game(game)

    def populate(self):

        games = [

            Game(
                title="Cyberpunk 2077",
                release_year=2020,
                platform=Platform(name="PC"),
                genre=Genre(name="Action RPG"),
                developer=Developer(name="CD Projekt RED"),
                state=GameState.PLAYING,
                playtime=32.5,
                rating=9.2,
                cover_path="assets/covers/cyberpunk_cover.jpg"
            ),

            Game(
                title="Resident Evil 4",
                release_year=2023,
                platform=Platform(name="PC"),
                genre=Genre(name="Survival Horror"),
                developer=Developer(name="Capcom"),
                state=GameState.COMPLETED,
                playtime=41.8,
                rating=9.1,
                cover_path="assets/covers/re4_cover.jpg"
            ),

            Game(
                title="Resident Evil 2",
                release_year=2019,
                platform=Platform(name="PC"),
                genre=Genre(name="Survival Horror"),
                developer=Developer(name="Capcom"),
                state=GameState.COMPLETED,
                playtime=18.2,
                rating=9.5,
                cover_path="assets/covers/re2_cover.jpg"
            ),

            Game(
                title="Marvel's Spider-Man Remastered",
                release_year=2022,
                platform=Platform(name="PlayStation 5"),
                genre=Genre(name="Action Adventure"),
                developer=Developer(name="Insomniac Games"),
                state=GameState.COMPLETED,
                playtime=35.4,
                rating=9.0,
                cover_path="assets/covers/spiderman_cover.jpg"
            ),

            Game(
                title="God of War",
                release_year=2018,
                platform=Platform(name="PlayStation 5"),
                genre=Genre(name="Action Adventure"),
                developer=Developer(name="Santa Monica Studio"),
                state=GameState.COMPLETED,
                playtime=54.3,
                rating=9.0,
                cover_path="assets/covers/gow_cover.jpg"
            ),

            Game(
                title="Ghost of Tsushima Director's Cut",
                release_year=2024,
                platform=Platform(name="PC"),
                genre=Genre(name="Action Adventure"),
                developer=Developer(name="Sucker Punch Productions"),
                state=GameState.COMPLETED,
                playtime=30.7,
                rating=9.7,
                cover_path="assets/covers/ghost_cover.jpg"
            ),

            Game(
                title="The Wolf Among Us",
                release_year=2013,
                platform=Platform(name="PC"),
                genre=Genre(name="Adventure"),
                developer=Developer(name="Telltale Games"),
                state=GameState.COMPLETED,
                playtime=14.6,
                rating=9.1,
                cover_path="assets/covers/wolf_cover.jpg"
            ),

            Game(
                title="Devil May Cry 5",
                release_year=2019,
                platform=Platform(name="Xbox"),
                genre=Genre(name="Hack and Slash"),
                developer=Developer(name="Capcom"),
                state=GameState.PLAYING,
                playtime=16.3,
                rating=9.3,
                cover_path="assets/covers/dmc_cover.jpg"
            ),

            Game(
                title="Dispatch",
                release_year=2025,
                platform=Platform(name="PC"),
                genre=Genre(name="Adventure"),
                developer=Developer(name="AdHoc Studio"),
                state=GameState.COMPLETED,
                playtime=10.5,
                rating=8.8,
                cover_path="assets/covers/dispatch_cover.jpg"
            ),

            Game(
                title="Clair Obscur: Expedition 33",
                release_year=2025,
                platform=Platform(name="PC"),
                genre=Genre(name="Turn-Based RPG"),
                developer=Developer(name="Sandfall Interactive"),
                state=GameState.PLAYING,
                playtime=52.7,
                rating=9.8,
                cover_path="assets/covers/clair_cover.jpg"
            )

        ]

        for game in games:
            self._add_if_not_exists(game)