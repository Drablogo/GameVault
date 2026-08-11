from models.platform import Platform
from models.genre import Genre
from models.developer import Developer
from models.game_state import GameState
from models.game import Game


def main():
    pc = Platform(None, "PC")
    rpg = Genre(None, "RPG")
    cdpr = Developer(None, "CD Projekt RED")

    game = Game(
        game_id = 1,
        title = "Cyberpunk 2077",
        release_year = 2020,
        platform=pc,
        genre=rpg,
        developer=cdpr,
        state=GameState.PLAYING,
        playtime=87.5,
        rating=9.2
    )

    print(game)

    game.update_rating(9.5)
    game.update_playtime(95.0)
    game.change_state(GameState.COMPLETED)

    print("\nAfter updates:\n")
    print(game)


if __name__ == "__main__":
    main()