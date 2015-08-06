# -*- coding: utf-8 -*-

from .label import *
from .lines import *


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

    def createLabel(self, text, x, y, size=36, font='Liberation Sans'):
        """
            Create a label contening text, at position (x, y)
        """
        self.items += [Label(text, x, y, size, font)]

    def createLines(self, x1, y1, x2, y2, origin=[0, 0]):
        """
            Create a line from (x1, y1) to (x2, y2)
        """
        self.items += [Lines(origin[0] + x1, origin[1] + y1,
                origin[0] + x2, origin[1] + y2)]