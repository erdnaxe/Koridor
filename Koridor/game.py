# -*- coding: utf-8 -*-
"""This is the Game class.
@author: Iooss
@license: MIT
"""

from board import *
from player import *
from case import *


class Game:
    """ Principal class of the game, controle everything relative to the game
    """

    def __init__(self):
        """ constructor
        """
        self.nbPlayer = 2
        self.idPlayer = 0  # active player

        self.board = Board()
        self.players = self.nbPlayer * [Player()]
        for player in self.players:
            player.init()
        #self.board.map[4][0].player = self.players[0]
        #self.board.map[4][9].player = self.players[1]

    def newGame(self):
        """ this fonction create a new game
        """
        self.__init__()

    def play(self, action):
        """
            Method to play an action and change the active player
            Return True if the action succeded, else False

            Exemples:
                play(action = "go_forward")
                play(action = "place_wall", coordWall=[[0, 0], 1])
        """
        # First, verify that the action is possible
        if not self.verifiedAction(action):
            return False

        # Do the action !
        if action == "go_forward":
            self.players[idPlayer].goForward()
        elif action == "go_backward":
            self.players[idPlayer].goBackward()
        elif action == "go_left":
            self.players[idPlayer].goLeft()
        elif action == "go_right":
            self.players[idPlayer].goRight()
        elif action == "place_wall":
            self.board.placeWall(coordWall)
        else:
            return 0

        # Change the active player
        if self.idPlayer != self.nbPlayer:
            self.idPlayer += 1
        else:
            self.idPlayer = 0

        return 1

    def verifiedAction(self, action):
        """
            Method to check if an action is possible
            Return True if yes, False if no
        """
        if action == "go_forward":
            return self.players[idPlayer].canGoForward()
        elif action == "go_backward":
            return self.players[idPlayer].canGoBackward()
        elif action == "go_to_left":
            return self.players[idPlayer].canGoToLeft()
        elif action == "go_to_right":
            return self.players[idPlayer].canGoToRight()
        elif action == "place_wall":
            return self.board.canPlaceWall(coordWall)
        else:
            return False

    def isFinnish():
        for player in self.players:
            if player.won():
                return player.id
        return 0
