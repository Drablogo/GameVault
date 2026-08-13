from database.game_repository import GameRepository
from database.genre_repository import GenreRepository
from database.platform_repository import PlatformRepository
from database.developer_repository import DeveloperRepository

class GameService:

    def __init__(self):

        self._game_repository = GameRepository()

        self._platform_repository = PlatformRepository()

        self._genre_repository = GenreRepository()

        self._developer_repository = DeveloperRepository()

    def get_all_games(self):
        return self._game_repository.get_all_games()

    def get_or_create_platform(self, name):

        platform = self._platform_repository.find_by_name(name)

        if platform:
            return platform

        self._platform_repository.add_platform(name)

        return self._platform_repository.find_by_name(name)

    def get_or_create_genre(self, name):

        genre = self._genre_repository.find_by_name(name)

        if genre:
            return genre

        self._genre_repository.add_genre(name)

        return self._genre_repository.find_by_name(name)

    def get_or_create_developer(self, name):

        developer = self._developer_repository.find_by_name(name)

        if developer:
            return developer

        self._developer_repository.add_developer(name)

        return self._developer_repository.find_by_name(name)



    def add_game(self, game):
        platform = self.get_or_create_platform(
            game.platform.name
        )

        genre = self.get_or_create_genre(
            game.genre.name
        )

        developer = self.get_or_create_developer(
            game.developer.name
        )

        game.platform.id = platform[0]
        game.genre.id = genre[0]
        game.developer.id = developer[0]

        self._game_repository.add_game(game)

    def get_game(self, game_id):
        return self._game_repository.get_game_by_id(game_id)

    def update_game(self, game):

        platform = self.get_or_create_platform(
            game.platform.name
        )

        genre = self.get_or_create_genre(
            game.genre.name
        )

        developer = self.get_or_create_developer(
            game.developer.name
        )

        game.platform.id = platform[0]
        game.genre.id = genre[0]
        game.developer.id = developer[0]

        self._game_repository.update_game(game)

    def delete_game(self, game_id):
        self._game_repository.delete_game(game_id)

    def game_exists(self, title: str):

        return self._game_repository.find_by_title(title) is not None