from models.game import Game

class Library:
    def __init__(self):
        self._games = []

    def add_game(self, game: Game):

        if not isinstance(game, Game):
            raise TypeError("Only Game objects can be added")

        if self.find_game_by_title(game.title):
            raise ValueError("A game with this title already exists.")

        self._games.append(game)

    def remove_game(self, game: Game):

        self._games.remove(game)

    def get_all_games(self):
        return self._games

    def find_game_by_title(self, title: str):
        for game in self._games:

            if game.title.lower() == title.lower():
                return game

        return None

    def total_games(self):
        return len(self._games)

    def __str__(self):
        if not self._games:
            return "Library is empty"

        return "\n\n".join(str(game) for game in self._games)

