# PacmanGame class, main loop

# game.py
import tkinter as tk
from pacman_game.pacman.settings import CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, MOVE_DELAY, DIRS
from pacman_game.pacman.entities import Pacman, Dot
from pacman_game.pacman.utils import cell_to_coords


class PacmanGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root,
            width=CELL_SIZE * GRID_WIDTH,
            height=CELL_SIZE * GRID_HEIGHT,
            bg='black')
        self.canvas.pack()

        self.score = 0
        self.score_text = self.canvas.create_text(
            5, 5, anchor='nw', fill='white',
            font=('Arial', 14), text='Score: 0')

        # create dots
        self.dots = {}
        for i in range(GRID_WIDTH):
            for j in range(GRID_HEIGHT):
                dot = Dot(self.canvas, i, j)
                self.dots[(i, j)] = dot

        # create Pacman
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.pacman = Pacman(self.canvas, start_x, start_y)
        self.direction = (0, 0)

        # key bindings
        root.bind('<Left>',  self.change_dir)
        root.bind('<Right>', self.change_dir)
        root.bind('<Up>',    self.change_dir)
        root.bind('<Down>',  self.change_dir)

        # start game loop
        self.move()

    def change_dir(self, event):
        if event.keysym in DIRS:
            self.direction = DIRS[event.keysym]

    def move(self):
        dx, dy = self.direction
        self.pacman.move(dx, dy)

        # eat dot
        pos = (self.pacman.x, self.pacman.y)
        if pos in self.dots:
            self.dots.pop(pos).remove()
            self.score += 1
            self.canvas.itemconfigure(
                self.score_text,
                text=f'Score: {self.score}'
            )

        # schedule next move
        self.root.after(MOVE_DELAY, self.move)
