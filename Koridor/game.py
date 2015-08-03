# -*- coding: utf-8 -*-
from board import *
from player import *
from case import *


class Game:

    def __init__(self):
        self.nbPlayer = 2
        self.idPlayer = 0 # rang du player qui joue

        self.board = Board()
        self.players = self.nbPlayer * [Player()]
        for player in self.players:
            player.init()
        #self.board.map[4][0].player = self.players[0]
        #self.board.map[4][9].player = self.players[1]

    def newGame(self):
        self.__init__()

    def play(self, action):
        if action == "go_forward":
            self.players[idPlayer].goForward()
            #self.board.map[4][0].player = None
            #self.board.map[4][1].player = self.players[0]
        elif action == "go_backward":
            self.board.map[4][0].player = None
            self.board.map[4][1].player = self.players[0]
        elif action == "go_to_left":
            self.board.map[4][0].player = None
            self.board.map[4][1].player = self.players[0]

        # continu si mouvement effectue, return 0 sinon
        if self.idPlayer = self.nbPlayer:
            self.idPlayer = 0
        else:
            self.idPlayer += 1

        return 1

    def verifiedAction(self, action):
        # return 1 si action possible, 0 sinon

    def isfinnish():
        # return id joueur si joueur a gagnié, sinon 0