# -*- coding: utf-8 -*-
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
