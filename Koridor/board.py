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
            Constructor
        """
        self.size = 9
        self.map = []
        self.players = players
        for i in range(self.size):
            self.map.append([Case()] * self.size)
        #TODO ajouter des murs autour du plateau

    def resetBoard(self):
        """
            Create a 2D array contenant des objets "case"
        """
        self.__init__()

    def getCase(self, x, y):
        """
            Return la case correspondant a la position
        """
        return self.map[x][y]

    def getPlayerByPosition(self, position):
        """
            return le joueur correspondant a la position
        """
        for player in self.players:
            if player.position == position:
                return player.id
        return 0

    def checkPath(self, positionPlayer, destinations):
        """
            Check if the player can go to his destinations
        """
        alreadyExplore = []
        self.resursiveCheckPath(positionPlayer, destinations, alreadyExplore)

    def resursiveCheckPath(self, position, destinations, alreadyExplore):
        """
            this method find a path
            position : [x,y]
        """
        if position in alreadyExplore:
            return False
        if position in destinations:
            return True

        alreadyExplore += [position]
        if not self.map[x][y].hasWall(1):
            if self.resursiveCheckPath([position[0], position[1] + 1],
                    destinations, alreadyExplore):
                return True

        if not self.map[x][y].hasWall(2):
            if self.resursiveCheckPath([position[0] + 1, position[1]],
                    destinations, alreadyExplore):
                return True

        if not self.map[x][y].hasWall(3):
            if self.resursiveCheckPath([position[0], position[1] - 1],
                    destinations, alreadyExplore):
                return True

        if not self.map[x][y].hasWall(4):
            if self.resursiveCheckPath([position[0] - 1, position[1]],
                    destinations, alreadyExplore):
                return True


        #TODO : appel de la fonction suivant les mur aux alentours