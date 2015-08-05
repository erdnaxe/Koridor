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
        self.activePlayer = 0  # joueur dont c'est le tour de jouer

        self.players = []
        for i in range(self.nbPlayer):
            self.players += [Player()]
        self.board = Board(self.players)

    def newGame(self):
        """ this fonction create a new game
        """
        self.__init__()

    def play(self, action):
        """
            Method to play an action and change the active player
            Return True if the action succeded, else False
        """

        # Do the action !
        if not self.players[self.activePlayer].executeAction(action):
            print("Cette action ne peut pas être effectué")
            return False

        # Change the active player
        if self.activePlayer != self.nbPlayer - 1:
            self.activePlayer += 1
        else:
            self.activePlayer = 0

        return True

    def isFinished(self):
        """
            This method checks if the game is finished
        """
        for player in self.players:
            if (player.initposition[0] - player.position[0]) ** 2 == 81:
                return player.id
        return 0
