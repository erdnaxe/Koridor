# -*- coding: utf-8 -*-
"""This is the Board class.
@author: Iooss
@license: MIT
"""

from case import *


class Board:
    def __init__(self, players):
        self.size = 9
        self.map = []
        self.players = players
        for i in range(self.size):
            self.map.append([Case()] * self.size)

    # Create a 2D array contenant des objets "case"
    def resetBoard(self):
        self.__init__()

    def getCase(self, x, y):
        return self.map[x][y]

    def getPlayerByCase(self, position):
        for player in self.players:
            if player.position == position:
                return player.id
