from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout
)

from services.game_service import GameService

from ui.game_details_widget import GameDetailsWidget
from ui.game_list_widget import GameListWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GameVault")
        self.resize(1200, 700)

        self._service = GameService()
        self._games = []

        self._apply_style()
        self._build_ui()

    def _apply_style(self):

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1b1b1b;
            }

            QWidget {
                background-color: #1b1b1b;
                color: white;
            }

            QListWidget {
                background-color: #292929;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 4px;
                font-size: 13px;
            }

            QListWidget::item {
                padding: 8px;
                border-radius: 4px;
            }

            QListWidget::item:selected {
                background-color: #3a3a3a;
                color: white;
            }

            QListWidget::item:hover {
                background-color: #333333;
            }
        """)

    def _build_ui(self):
        central_widget = QWidget()

        central_widget.setStyleSheet("""
            background-color: #1b1b1b;
        """)

        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        layout.setContentsMargins(
            10,
            10,
            10,
            10
        )

        layout.setSpacing(15)

        central_widget.setLayout(layout)

        # =========================
        # LEFT PANEL
        # =========================

        self.game_list = GameListWidget()

        # =========================
        # RIGHT PANEL
        # =========================

        self.details = GameDetailsWidget()

        layout.addWidget(
            self.game_list,
            1
        )

        layout.addWidget(
            self.details,
            3
        )

        # =========================
        # LOAD GAMES
        # =========================

        self._load_games()

        self.game_list.currentRowChanged.connect(
            self._show_game_details
        )

    def _load_games(self):

        self._games = self._service.get_all_games()

        self.game_list.load_games(
            self._games
        )

    def _show_game_details(self, index):

        game = self.game_list.get_selected_game()

        if game is None:
            return

        self.details.display_game(game)