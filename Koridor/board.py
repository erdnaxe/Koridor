# -*- coding: utf-8 -*-
from case import *


class Board:
    def __init__(self):
        self.resetBoard()

    # Create a 2D array with "case" objects
    def resetBoard(self):
        self.map = []
        for i in range(10):
            self.map.append([Case()] * 10)
