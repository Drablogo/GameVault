from enum import Enum


class GameState(Enum):
    TO_PLAY = "To Play"
    PLAYING = "Playing"
    COMPLETED = "Completed"

    def __str__(self):
        return self.value