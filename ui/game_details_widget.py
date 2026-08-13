from ui.cover_widget import CoverWidget
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

class GameDetailsWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            GameDetailsWidget {
                background-color: #1b1b1b;
            }

            QLabel {
                color: white;
            }
        """)

        self._build_ui()

    def _build_ui(self):

        # =========================
        # COVER
        # =========================

        self.cover = CoverWidget()

        # =========================
        # TITLE
        # =========================

        self.title_label = QLabel()

        self.title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
        """)

        # =========================
        # DETAILS
        # =========================

        self.release_year_label = self._create_value_label()
        self.platform_label = self._create_value_label()
        self.genre_label = self._create_value_label()
        self.developer_label = self._create_value_label()
        self.state_label = self._create_value_label()
        self.playtime_label = self._create_value_label()
        self.rating_label = self._create_value_label()

        # =========================
        # DETAILS LAYOUT
        # =========================

        details_layout = QVBoxLayout()

        details_layout.setSpacing(14)

        details_layout.addWidget(
            self.title_label
        )

        details_layout.addSpacing(10)

        details_layout.addWidget(
            self._create_detail(
                "Release Year",
                self.release_year_label
            )
        )

        details_layout.addWidget(
            self._create_detail(
                "Platform",
                self.platform_label
            )
        )

        details_layout.addWidget(
            self._create_detail(
                "Genre",
                self.genre_label
            )
        )

        details_layout.addWidget(
            self._create_detail(
                "Developer",
                self.developer_label
            )
        )

        details_layout.addWidget(
            self._create_detail(
                "State",
                self.state_label
            )
        )

        details_layout.addWidget(
            self._create_detail(
                "Playtime",
                self.playtime_label
            )
        )

        details_layout.addWidget(
            self._create_detail(
                "Rating",
                self.rating_label
            )
        )

        # =========================
        # MAIN LAYOUT
        # =========================

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            40,
            30,
            40,
            30
        )

        layout.setSpacing(40)

        layout.addWidget(
            self.cover,
            alignment=Qt.AlignmentFlag.AlignVCenter
        )

        layout.addLayout(details_layout)

        layout.addStretch()

    def _create_value_label(self):

        label = QLabel()

        label.setStyleSheet("""
            font-size: 14px;
            color: white;
        """)

        return label

    def _create_detail(
        self,
        title,
        value_label
    ):

        container = QWidget()

        layout = QVBoxLayout(container)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(2)

        title_label = QLabel(title)

        title_label.setStyleSheet("""
            font-size: 12px;
            color: #999999;
        """)

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            value_label
        )

        return container

    def display_game(self, game):
        self.cover.set_cover(
            game.cover_path
        )

        self.title_label.setText(
            game.title
        )

        self.release_year_label.setText(
            str(game.release_year)
        )

        self.platform_label.setText(
            game.platform.name
        )

        self.genre_label.setText(
            game.genre.name
        )

        self.developer_label.setText(
            game.developer.name
        )

        self.state_label.setText(
            game.state.value
        )

        self.playtime_label.setText(
            f"{game.playtime:.1f} h"
        )

        self.rating_label.setText(
            f"{game.rating:.1f} ⭐"
        )