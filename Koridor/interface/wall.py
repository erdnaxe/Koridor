# -*- coding: utf-8 -*-

from .lines import *


class Wall:

    def __init__(self, coord, side, grid):
        """
            Constructor
        """
        color = [255, 0, 0]
        width = 3

        # Origin coords of the case
        x = coord[0] * grid.width // grid.size_x
        y = coord[1] * grid.height // grid.size_y

        if side == 1:
            x2 = x + grid.width // grid.size_x
            y1 = y + grid.width // grid.size_y
            self.line = Lines(x, y1, x2, y1, grid.origin, color, width)
        elif side == 2:
            x1 = x + grid.width // grid.size_x
            y2 = y + grid.width // grid.size_y
            self.line = Lines(x1, y, x1, y2, grid.origin, color, width)
        elif side == 3:
            x2 = x + grid.width // grid.size_x
            self.line = Lines(x, y, x2, y, grid.origin, color, width)
        else:
            y2 = y + grid.width // grid.size_y
            self.line = Lines(x, y, x, y2, grid.origin, color, width)

    def draw(self):
        """
            Draw the object
        """
        self.line.draw()
