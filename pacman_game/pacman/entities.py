# Dot, Ghost, Pacman
# Other variance
import tkinter as tk
from pacman_game.pacman.settings import CELL_SIZE, GRID_WIDTH, GRID_HEIGHT
from pacman_game.pacman.utils import cell_to_coords


class Pacman:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = self.canvas.create_oval(*cell_to_coords(x, y), fill='yellow')

    def move(self, dx, dy):
        # wrap-around
        self.x = (self.x + dx) % GRID_WIDTH
        self.y = (self.y + dy) % GRID_HEIGHT
        self.canvas.coords(self.id, *cell_to_coords(self.x, self.y))


class Dot:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        cx = x * CELL_SIZE + CELL_SIZE // 2
        cy = y * CELL_SIZE + CELL_SIZE // 2
        self.id = self.canvas.create_oval(cx-3, cy-3, cx+3, cy+3, fill='white')

    def remove(self):
        self.canvas.delete(self.id)


class Ghost:
    def __init__(self, canvas, x, y, color='red'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = self.canvas.create_rectangle(*cell_to_coords(x, y), fill=color)

    # movement and AI logic can be added here
