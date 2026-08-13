from PyQt6.QtWidgets import QListWidget


class GameListWidget(QListWidget):

    def __init__(self):
        super().__init__()

        self._games = []

    def load_games(self, games):

        self.clear()

        self._games = games

        for game in games:
            self.addItem(game.title)

        if games:
            self.setCurrentRow(0)

    def get_selected_game(self):

        index = self.currentRow()

        if index < 0:
            return None

        return self._games[index]