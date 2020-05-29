
from system import Game

from system import Keyboard
from system import Moving
from system import Painting
from system import Rotating
from system import Respawn

from system import MobFactory
from system import SceneFactory

from logcat import LogCat

def main():
    game = Game()

    for system in (
        Keyboard, Moving, Painting, Rotating, Respawn,
        MobFactory, SceneFactory,
    ):
        system()

    game.start()

if __name__ == "__main__":
    main()

# shot.py
