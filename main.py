import sys

from PyQt6.QtWidgets import QApplication

from database.schema import Schema
from database.seed import Seed
from ui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    schema = Schema()
    schema.create_tables()

    seed = Seed()
    seed.populate()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()