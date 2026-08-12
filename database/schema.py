from database.database import Database

class Schema:
    def __init__(self):
        self._database = Database()

    def create_tables(self):
        connection = self._database.connect()

        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS platforms (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL UNIQUE

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS genres (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL UNIQUE

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS developers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL UNIQUE

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            release_year INTEGER NOT NULL,

            platform_id INTEGER NOT NULL,

            genre_id INTEGER NOT NULL,

            developer_id INTEGER NOT NULL,

            state TEXT NOT NULL,

            playtime REAL DEFAULT 0,

            rating REAL DEFAULT 0,

            cover_path TEXT,

            FOREIGN KEY (platform_id) REFERENCES platforms(id),

            FOREIGN KEY (genre_id) REFERENCES genres(id),

            FOREIGN KEY (developer_id) REFERENCES developers(id)

        )
        """)

        connection.commit()

        self._database.close()
