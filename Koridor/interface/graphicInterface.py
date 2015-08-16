# -*- coding: utf-8 -*-

from .windowFactory import *


class GraphicInterface:
    """
        Graphic interface of the game, created with OpenGL
        It used PyGlet to bind OpenGL to Python
    """

    def __init__(self, game, width=200, height=200):
        """
            Constructor
        """
        self.factory = WindowFactory()  # Factory
        self.factory.createLabel('Koridor', 0, 300)  # Title
        self.grid = self.factory.createGrid(game.board, width, height)  # Grid

        # Get players & walls
        self.players = game.players
        self.map = game.board.map

        # Place players & walls
        self.refresh()

    def refresh(self):
        """
            Method to refresh the interface
        """
        self.factory.removePlayers()
        for player in self.players:
            self.factory.createPlayer(player, self.grid)
