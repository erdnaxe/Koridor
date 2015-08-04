# -*- coding: utf-8 -*-
"""This is the Board class.
@author: Iooss
@license: MIT
"""

from case import *


class Board:
    """
    this method implement the board of the game
    """
    def __init__(self, players):
        """
        constructor
        """
        self.size = 9
        self.map = []
        self.players = players
        for i in range(self.size):
            self.map.append([Case()] * self.size)

    def resetBoard(self):
        """
            Create a 2D array contenant des objets "case"
        """
        self.__init__()

    def getCase(self, x, y):
        """
            retourne la case correspondant a la position
        """
        return self.map[x][y]

    def getPlayerByPosition(self, position):
        """
            return le joueur correspondant a la position
        """
        for player in self.players:
            if player.position == position:
                return player.id
