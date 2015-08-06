# -*- coding: utf-8 -*-

from .label import *
from .lines import *
from .grid import *


class WindowFactory:
    """
        Factory to simplify drawing object with OpenGL
    """

    def __init__(self):
        """
            Constructor
        """
        self.window = pyglet.window.Window()
        self.items = []

    def draw(self):
        """
            Clear and then draw all objects
        """
        self.window.clear()
        for item in self.items:
            item.draw()
        self.grid.draw()

    def createLabel(self, text, x, y, size=36, font='Liberation Sans'):
        """
            Create a label contening text, at position (x, y)
        """
        self.items += [Label(text, x, y, size, font)]

    def createLines(self, x1, y1, x2, y2, origin=[0, 0]):
        """
            Create a line from (x1, y1) to (x2, y2)
        """
        self.items += [Lines(x1, y1, x2, y2, origin)]

    def createGrid(self, size_x, size_y, width, height):
        """
            Create a grid of size size_x, size_y
        """
        self.grid = Grid(size_x, size_y, width, height)