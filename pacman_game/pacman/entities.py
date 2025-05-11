# entities.py
import random
from pacman.settings import GRID_WIDTH, GRID_HEIGHT
from pacman.utils import load_sprite, cell_to_pixel, get_rotated_sprite


class Pacman:
    def __init__(self, canvas, i, j):
        self.canvas = canvas
        self.i = i
        self.j = j
        self.dir = (1, 0)
        self.open = False
        # initial sprite
        img = get_rotated_sprite('pacman_open', self.open, self.dir)
        self.id = canvas.create_image(*cell_to_pixel(i, j), image=img)

    def set_direction(self, dx, dy):
        """Update direction and immediately rotate Pac-Man to face it."""
        self.dir = (dx, dy)
        # update sprite orientation without toggling mouth
        img = get_rotated_sprite('pacman_open', self.open, self.dir)
        self.canvas.itemconfigure(self.id, image=img)

    def move_one_cell(self, passable):
        dx, dy = self.dir
        ni = (self.i + dx) % GRID_WIDTH
        nj = (self.j + dy) % GRID_HEIGHT
        if passable(ni, nj):
            self.i, self.j = ni, nj
            self.open = not self.open
            img = get_rotated_sprite('pacman_open', self.open, self.dir)
            self.canvas.itemconfigure(self.id, image=img)
            self.canvas.coords(self.id, *cell_to_pixel(self.i, self.j))


class Ghost:
    def __init__(self, canvas, i, j, color='red'):
        self.canvas = canvas
        self.i = i
        self.j = j
        # random initial direction
        self.dir = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        # load ghost sprite
        self.img = load_sprite(f'ghost_{color}')
        # place at cell center
        x, y = cell_to_pixel(self.i, self.j)
        self.id = canvas.create_image(x, y, image=self.img)

    def move_one_cell(self, passable):
        dx, dy = self.dir
        # compute candidate cell
        ni = (self.i + dx) % GRID_WIDTH
        nj = (self.j + dy) % GRID_HEIGHT
        # if blocked, pick a new valid direction
        if not passable(ni, nj):
            choices = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(choices)
            for dx2, dy2 in choices:
                ni2 = (self.i + dx2) % GRID_WIDTH
                nj2 = (self.j + dy2) % GRID_HEIGHT
                if passable(ni2, nj2):
                    self.dir = (dx2, dy2)
                    ni, nj = ni2, nj2
                    break
        # update position
        self.i, self.j = ni, nj
        # snap to cell center
        x, y = cell_to_pixel(self.i, self.j)
        self.canvas.coords(self.id, x, y)
