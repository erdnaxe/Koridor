# -*- coding: utf-8 -*-
from .label import *


class Player():

    def __init__(self, player, grid):
        """
            Constructor
        """
        x = player.position[0] * grid.width // grid.size_x
        y = player.position[1] * grid.height // grid.size_y

        x += grid.origin[0] + grid.case_width // 4
        y += grid.origin[1] + grid.case_height // 4

        text_height = grid.case_height // 2

        self.label = Label(str(player.id), x, y, text_height)

    def draw(self):
        """
            Draw the object
        """
        self.label.draw()
