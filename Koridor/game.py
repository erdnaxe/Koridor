# -*- coding: utf-8 -*-
from board import *
from player import *
from case import *


class Game:

    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.board.map[4][0].player = self.players[0]
        self.board.map[4][9].player = self.players[1]

    def newGame(self):
        self.__init__()

    def play(self, action):
        if action == "go_forward":
            self.board.map[4][0].player = None
            self.board.map[4][1].player = self.players[0]
        else if action == "go_backward":
            self.board.map[4][0].player = None
            self.board.map[4][1].player = self.players[0]
        else if action == "go_to_left":
            self.board.map[4][0].player = None
            self.board.map[4][1].player = self.players[0]

        #return 1 si mouvement effectue, 0 sinon

    def verifiedAction(self, action):
        # return 1 si action possible, 0 sinon

    def isfinnish():
        # return id joueur si joueur a gagnié, sinon 0