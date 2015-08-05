# -*- coding: utf-8 -*-
"""This is the Game class.
@author: Iooss
@license: MIT
"""

from board import *
from player import *
from case import *
from action import *


class Game:
    """ Principal class of the game, controle everything relative to the game
    """

    def __init__(self):
        """ constructor
        """
        self.nbPlayer = 2
        self.activePlayer = 0

        self.players = []
        for i in range(self.nbPlayer):
            self.players += [Player()]
        self.action = Action()
        self.board = Board(self.players)

    def newGame(self):
        """ this fonction create a new game
        """
        self.__init__()

    def play(self, actionString):
        """
            Method to play an action and change the active player
            Return True if the action succeded, else False

            Exemples:
                play(action = "go_forward")
                play(action = "place_wall", coordWall=[[0, 0], 1])
        """
        self.action.stringToAction()

        # First, verify that the action is possible
        if not self.verifiedAction(self.action):
        #TODO modifier
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
        if self.activePlayer != self.nbPlayer:
            self.activePlayer += 1
        else:
            self.activePlayer = 0

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

    def isFinished(self):
        for player in self.players:
            if (player.initPosition[0] - player.position[0]) == 9:
                return player.id
            if (player.position[0] - player.initPosition[0]) == 9:
                return player.id
        return 0
