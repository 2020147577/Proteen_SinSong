# game.py
import tkinter as tk
from pacman.settings import (
    MAP_LAYOUT, CELL_SIZE, WINDOW_SIZE,
    PACMAN_DELAY, GHOST_DELAY, LOGO_COLOR,
    BG_COLOR, WALL_COLOR, INITIAL_LIVES
)
from pacman.utils import load_sprite, cell_to_pixel
from pacman.entities import Pacman, Ghost


class PacmanGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1], bg=BG_COLOR)
        self.canvas.pack()

        # walls and pellets
        self.walls = set()
        self.pellets = set()
        self.pellet_ids = {}
        for j, row in enumerate(MAP_LAYOUT):
            for i, ch in enumerate(row):
                x1 = i * CELL_SIZE
                y1 = j * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                '''
                실습 1: $ 부분의 색을 변경하기
                현재, 바로 아래 if문이 #, $인 경우 모두를 담당
                새로 elif문을 만들어서 $의 경우를 별도 처리하도록 한다
                Hint: 노란색으로 바꾸기 위해서 settings.py의 가장 아래부분을 참고
                '''
                if ch == '#' or ch == '$':
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill=WALL_COLOR, width=0
                    )
                    self.walls.add((i, j))
                # TODO: 이 사이에 새로운 elif를 넣어서 환성
                elif ch in ('.', 'o'):
                    key = 'pellet' if ch == '.' else 'power_pellet'
                    img = load_sprite(key)
                    pid = self.canvas.create_image(
                        x1 + CELL_SIZE // 2,
                        y1 + CELL_SIZE // 2,
                        image=img
                    )
                    self.pellets.add((i, j))
                    self.pellet_ids[(i, j)] = pid

        # actors
        self.pacman = Pacman(self.canvas, 1, 1)
        self.ghosts = [Ghost(self.canvas, 12, 11, 'red'),
                       Ghost(self.canvas, 12, 13, 'blue')]

        # game state
        self.running = True
        self.lives = INITIAL_LIVES
        self.score = 0

        # UI text
        self.score_txt = self.canvas.create_text(5, 5, anchor='nw', fill='white', font=('Arial', 14),
                                                 text=f'Score: {self.score}')
        self.lives_txt = self.canvas.create_text(5, 25, anchor='nw', fill='white', font=('Arial', 14),
                                                 text=f'Lives: {self.lives}')

        # input
        root.bind('<Left>', lambda e: self.pacman.set_direction(-1, 0))
        root.bind('<Right>', lambda e: self.pacman.set_direction(1, 0))
        root.bind('<Up>', lambda e: self.pacman.set_direction(0, -1))
        root.bind('<Down>', lambda e: self.pacman.set_direction(0, 1))

        # start loops
        self.root.after(PACMAN_DELAY, self.move_pacman)
        self.root.after(GHOST_DELAY, self.move_ghosts)

    def passable(self, i, j):
        return (i, j) not in self.walls

    def move_pacman(self):
        if not self.running: return
        self.pacman.move_one_cell(self.passable)
        pos = (self.pacman.i, self.pacman.j)
        if pos in self.pellets:
            self.pellets.remove(pos)
            self.canvas.delete(self.pellet_ids.pop(pos))
            self.score += 10
            self.canvas.itemconfigure(self.score_txt, text=f'Score: {self.score}')
            # win condition
            if not self.pellets:
                self.game_win()
                return
        # collision with ghosts
        for g in self.ghosts:
            if (g.i, g.j) == (self.pacman.i, self.pacman.j):
                self.lives -= 1
                self.canvas.itemconfigure(self.lives_txt, text=f'Lives: {self.lives}')
                if self.lives > 0:
                    # reset Pac-Man to start
                    self.pacman.i, self.pacman.j = 1, 1
                    self.canvas.coords(self.pacman.id, *cell_to_pixel(1, 1))
                else:
                    self.game_over()
                    return
        self.root.after(PACMAN_DELAY, self.move_pacman)

    def move_ghosts(self):
        if not self.running: return
        for g in self.ghosts:
            g.move_one_cell(self.passable)
            if (g.i, g.j) == (self.pacman.i, self.pacman.j):
                self.lives -= 1
                self.canvas.itemconfigure(self.lives_txt, text=f'Lives: {self.lives}')
                if self.lives > 0:
                    self.pacman.i, self.pacman.j = 1, 1
                    self.canvas.coords(self.pacman.id, *cell_to_pixel(1, 1))
                else:
                    self.game_over()
                    return
        self.root.after(GHOST_DELAY, self.move_ghosts)

    def game_over(self):
        self.running = False
        w, h = WINDOW_SIZE
        self.canvas.create_text(w // 2, h // 2, text='GAME OVER', fill='red', font=('Arial', 32, 'bold'))

    def game_win(self):
        self.running = False
        w, h = WINDOW_SIZE
        self.canvas.create_text(w // 2, h // 2, text='YOU WIN!', fill='yellow', font=('Arial', 32, 'bold'))
