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
        '''
        실습 2: 고스트가 벽에 부딪히는 경우가 아니더라도 방향을 매번 변경할 수 있도록 한다!
        Hint: 아래 if문은 passable하지 않은 경우에만 방향을 변경할 수 있도록 되어 있음
        -> 그것과 무관하게 항상 방향을 변경할 수 있도록 수정!
        
        실습 3(도전!): 실습 2에서 앞뒤로 진동하듯이 고스트가 움직이는 현상을 방지하도록 갈림길에서만 방향을 변경!
        Hint: 고스트가 현재 갈림길에 있다면 passable = True인 choices가 적어도 3개일 것!
        '''
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
