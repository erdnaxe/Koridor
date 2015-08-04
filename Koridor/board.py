# -*- coding: utf-8 -*-
"""This is the Board class.
@author: Iooss
@license: MIT
"""

from case import *


class Board:
    def __init__(self):
        self.size = 9
        self.map = []
        for i in range(self.size):
            self.map.append([Case()] * self.size)

    # Create a 2D array contenant des objets "case"
    def resetBoard(self):
        self.__init__()

    def getCase(self, x, y):
        return self.map[x][y]
