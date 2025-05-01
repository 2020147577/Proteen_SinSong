# grid ↔ canvas coords, collision checks
from pacman_game.pacman.settings import CELL_SIZE


def cell_to_coords(i, j):
    """
    Convert grid cell (i, j) to canvas coords (x1, y1, x2, y2).
    """
    x1 = i * CELL_SIZE + 2
    y1 = j * CELL_SIZE + 2
    x2 = x1 + CELL_SIZE - 4
    y2 = y1 + CELL_SIZE - 4
    return x1, y1, x2, y2
