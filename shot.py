
from game import Game

from system import Keyboard
from system import Moving
from system import Painting
from system import Rotating

from logcat import LogCat

def main():
    game = Game()

    for system in (
        Keyboard, Moving, Painting, Rotating
    ):
        system()

    game.start()

if __name__ == "__main__":
    main()

# shot.py
