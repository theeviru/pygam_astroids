from pygame.image import load
from pygame.math import Vector2
from pathlib import Path

def load_sprite(name, with_alpha=True):
    filename = Path(__file__).parent / Path("sprites/" + name + ".png")
    sprite = load(filename.resolve())

    if with_alpha:
        return sprite.convert_alpha()

    return sprite.convert()

def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)