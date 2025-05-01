import unittest
from pacman_game.pacman import entities, settings, utils


class FakeCanvas:
    """Minimal Canvas shim for testing coords and delete calls."""
    def __init__(self):
        self.items = {}
        self.next_id = 1
        self.last_text = None

    def create_oval(self, *args, **kwargs):
        obj_id = self.next_id
        self.next_id += 1
        self.items[obj_id] = ('oval', args, kwargs)
        return obj_id

    def delete(self, obj_id):
        # simulate removing the dot
        self.items.pop(obj_id, None)

    def coords(self, obj_id, *args):
        # record updated coords
        self.items[obj_id] = ('coords', args)

    def itemconfigure(self, text=None, **kwargs):
        self.last_text = kwargs.get('text', text)


class TestUtils(unittest.TestCase):
    def test_cell_to_coords(self):
        # for cell (0,0)
        x1, y1, x2, y2 = utils.cell_to_coords(0, 0)
        # should be within first CELL_SIZE block
        self.assertTrue(0 <= x1 < x2 <= settings.CELL_SIZE)
        self.assertTrue(0 <= y1 < y2 <= settings.CELL_SIZE)


class TestPacmanMovement(unittest.TestCase):
    def setUp(self):
        self.canvas = FakeCanvas()
        # place Pac-Man at (0,0)
        self.p = entities.Pacman(self.canvas, 0, 0)

    def test_wrap_around(self):
        # move left from x=0 should wrap to GRID_WIDTH-1
        self.p.move(-1, 0)
        self.assertEqual(self.p.x, settings.GRID_WIDTH - 1)
        # move up from y=0 should wrap to GRID_HEIGHT-1
        self.p.move(0, -1)
        self.assertEqual(self.p.y, settings.GRID_HEIGHT - 1)

    def test_coords_update(self):
        # store old id entry
        old = self.canvas.items[self.p.id]
        self.p.move(1, 0)
        self.assertNotEqual(self.canvas.items[self.p.id], old)


class TestDotEating(unittest.TestCase):
    def setUp(self):
        self.canvas = FakeCanvas()
        # create one dot at (1,0)
        self.dot = entities.Dot(self.canvas, 1, 0)

    def test_dot_remove(self):
        dot_id = self.dot.id
        self.dot.remove()
        self.assertNotIn(dot_id, self.canvas.items)
