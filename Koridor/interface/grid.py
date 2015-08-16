# -*- coding: utf-8 -*-
from .lines import *


class Grid():
    """
        Class to create objects to draw the grid
    """

    def __init__(self, board, width, height):
        """
            Constructor
        """
        self.items = []

        self.width = width
        self.height = height
        self.size_x = board.size
        self.size_y = board.size
        self.origin = [50, 50]

        # Draw vertical lines
        self.case_width = int(width // self.size_x)
        for i in range(self.size_x - 1):
            x = self.case_width * (i + 1)
            self.items += [Lines(x, height, x, 0, self.origin)]

        # Draw horizontal lines
        self.case_height = int(height // self.size_y)
        for i in range(self.size_y - 1):
            y = self.case_height * (i + 1)
            self.items += [Lines(0, y, width, y, self.origin)]

    def draw(self):
        """
            Draw the grid
        """
        for item in self.items:
            item.draw()

    def getCaseByAbsolutCoordinates(self, x, y):
        """
            Method to get the cooresponding case to a coordinate
        """
        x = x - self.origin[0]
        y = y - self.origin[1]
        case_x = x * self.size_x // self.width
        case_y = y * self.size_y // self.height

        if not case_x > (self.size_x - 1) and not case_y > (self.size_y - 1):
            if not case_x < 0 and not case_y < 0:
                return [case_x, case_y]