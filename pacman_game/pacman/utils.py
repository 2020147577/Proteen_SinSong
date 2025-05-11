import os
from collections import Counter
from PIL import Image, ImageTk
import tkinter as tk

from pacman.settings import IMAGE_ASSETS, CELL_SIZE

# locate assets/images folder relative to this file
HERE = os.path.dirname(__file__)
ASSETS = os.path.abspath(os.path.join(HERE, '..', 'assets', 'images'))


def trim_pacman_image(source_name, out_name, tol=10):
    # load & crop
    sheet_path = os.path.join(ASSETS, source_name)
    sheet = Image.open(sheet_path).convert('RGBA')
    w, h = sheet.size
    pixels = sheet.load()

    # sample border pixels to determine background color
    border_colors = []
    for x in range(w):
        border_colors.append(pixels[x, 0][:3])
        border_colors.append(pixels[x, h - 1][:3])
    for y in range(h):
        border_colors.append(pixels[0, y][:3])
        border_colors.append(pixels[w - 1, y][:3])
    bg_color, _ = Counter(border_colors).most_common(1)[0]

    # remove bg pixels
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if (abs(r - bg_color[0]) <= tol and
                    abs(g - bg_color[1]) <= tol and
                    abs(b - bg_color[2]) <= tol):
                pixels[x, y] = (0, 0, 0, 0)

    # trim to non-zero-alpha bbox
    alpha = sheet.split()[3]
    bbox = alpha.getbbox()
    trimmed = sheet.crop(bbox)

    # save output
    out_path = os.path.join(ASSETS, f"{out_name}.png")
    trimmed.save(out_path)
    print(f"→ Saved trimmed sprite: {out_path}")


# caches
_RAW_CACHE = {}
_TK_CACHE  = {}


def load_raw_sprite(name):
    """Return a resized PIL.Image for sprite 'name'."""
    if name not in _RAW_CACHE:
        path = os.path.join(
            os.path.dirname(__file__), '..', 'assets', 'images', IMAGE_ASSETS[name]
        )
        pil = Image.open(path).convert('RGBA')
        # high-quality resize
        try:
            resample = Image.Resampling.LANCZOS
        except AttributeError:
            resample = Image.LANCZOS
        pil = pil.resize((CELL_SIZE, CELL_SIZE), resample)
        _RAW_CACHE[name] = pil
    return _RAW_CACHE[name]


def get_rotated_sprite(name, open_frame, direction):
    """
    Return a PhotoImage for Pac-Man (open or closed) rotated to 'direction'.
    direction: (dx,dy)
    """
    key = (name, open_frame, direction)
    if key not in _TK_CACHE:
        pil_open   = load_raw_sprite('pacman_open')
        pil_closed = load_raw_sprite('pacman_closed')
        base = pil_open if open_frame else pil_closed
        dx, dy = direction
        # map grid direction to rotation angle:
        # +x (right) = 0°, -x (left) = 180°, -y (up) = 90°, +y (down) = 270°
        if dx > 0:
            angle = 0
        elif dx < 0:
            angle = 180
        elif dy < 0:
            angle = 90
        elif dy > 0:
            angle = 270
        else:
            angle = 0
        rot = base.rotate(angle, expand=False)
        _TK_CACHE[key] = ImageTk.PhotoImage(rot)
    return _TK_CACHE[key]


def load_sprite(name):
    """Return a PhotoImage for a static sprite (no rotation)."""
    if name not in _TK_CACHE:
        pil = load_raw_sprite(name)
        _TK_CACHE[name] = ImageTk.PhotoImage(pil)
    return _TK_CACHE[name]


def cell_to_pixel(i, j):
    """Return the (x,y) center pixel of cell (i,j)."""
    x = i * CELL_SIZE + CELL_SIZE//2
    y = j * CELL_SIZE + CELL_SIZE//2
    return x, y


# assign CELL_SIZE dynamically
cell_to_pixel.CELL = CELL_SIZE

if __name__ == '__main__':
    trim_pacman_image("pacman_open.png", "pacman_open_out")
    trim_pacman_image("pacman_closed.png", "pacman_closed_out")
