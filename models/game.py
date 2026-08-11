from datetime import datetime

from models.platform import Platform
from models.genre import Genre
from models.developer import Developer
from models.game_state import GameState

class Game:
    def __init__(
            self,
            game_id: int,
            title: str,
            release_year: int,
            platform: Platform,
            genre: Genre,
            developer: Developer,
            state: GameState,
            playtime: float = 0.0,
            rating: float = 0.0
    ):

        self._id = game_id
        self.title = title
        self.release_year = release_year
        self.platform = platform
        self.genre = genre
        self.developer = developer
        self.state = state
        self.playtime = playtime
        self.rating = rating

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        value = value.strip()

        if not value:
            raise ValueError("Game Title cannot be empty")

        self._title = value

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, value):

        current_year = datetime.now().year

        if value < 1958 or value > current_year:
            raise ValueError("| Invalid release year | Game Release Year must be between 1958 and current year |")

        self._release_year = value

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):

        if not isinstance(value, Platform):
            raise TypeError("| Invalid platform type | Platform must be a Platform object |")

        self._platform = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):

        if not isinstance(value, Genre):
            raise TypeError("| Invalid genre type | Genre must be a Genre object |")

        self._genre = value

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, value):

        if not isinstance(value, Developer):
            raise TypeError("| Invalid developer type | Developer must be a Developer object |")

        self._developer = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):

        if not isinstance(value, GameState):
            raise TypeError("State must be a GameState value.")

        self._state = value

    @property
    def playtime(self):
        return self._playtime

    @playtime.setter
    def playtime(self, value):

        if value < 0:
            raise ValueError("| Invalid playtime value | Game Playtime cannot be negative |")

        self._playtime = float(value)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):

        if value < 0 or value > 10:
            raise ValueError("| Invalid rating value | Game Rating must be between 0 and 10 |")

        self._rating = float(value)

    def update_rating(self, rating: float):
        self.rating = rating

    def update_playtime(self, hours: float):
        self.playtime = hours

    def change_state(self, state: GameState):
        self.state = state

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Release Year: {self.release_year}\n"
            f"Platform: {self.platform}\n"
            f"Genre: {self.genre}\n"
            f"Developer: {self.developer}\n"
            f"State: {self.state}\n"
            f"Playtime: {self.playtime:.1f} hours\n"
            f"Rating: {self.rating:.1f}/10"
        )