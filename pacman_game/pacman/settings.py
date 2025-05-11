# settings.py
import os
from PIL import Image


def load_map():
    # Larger map layout: '#'=wall, '.'=pellet, 'o'=power pellet, ' '=empty
    return [
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#o####.#####.##.#####.####o#",
        "#.####.#####.##.#####.####.#",
        "#..........................#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.##### ## #####.######",
        "     #.##### ## #####.#     ",
        "     #.##          ##.#     ",
        "######.## ######## ##.######",
        "     .   ########   .     ",
        "######.## ######## ##.######",
        "     #.##          ##.#     ",
        "     #.## ######## ##.#     ",
        "######.## ######## ##.######",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#o####.#####.##.#####.####o#",
        "#..##..................##..#",
        "##.##.##.##########.##.##.##",
        "#......#.....##.....#......#",
        "#.#######.##.##.##.#######.#",
        "#..........................#",
        "############################",
    ]

# Map layout
MAP_LAYOUT  = load_map()
GRID_HEIGHT = len(MAP_LAYOUT)
GRID_WIDTH  = len(MAP_LAYOUT[0])

# Image assets (filenames in assets/images/)
IMAGE_ASSETS = {
    'pacman_open':   'pacman_open.png',
    'pacman_closed': 'pacman_closed.png',
    'ghost_red':     'ghost_red.png',
    'ghost_blue':    'ghost_blue.png',
    'pellet':        'pellet.png',
    'power_pellet':  'power_pellet.png',
}

# Determine cell size from the 'pacman_open' sprite
ASSETS_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'assets', 'images'
))
_pac = Image.open(os.path.join(ASSETS_DIR, IMAGE_ASSETS['pacman_open']))
CELL_SIZE = 30

# Derived settings
WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)

# Timing (grid ticks)
PACMAN_DELAY = 120    # ms per Pac-Man hop
GHOST_DELAY  = 200    # ms per Ghost hop

# Gameplay settings
INITIAL_LIVES = 3     # Number of lives for Pac-Man

# Colors
WALL_COLOR = 'navy'
BG_COLOR   = 'black'
