# -*- coding: utf-8 -*-

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *

from .windowFactory import *


class GraphicInterface:
    """
        Graphic interface of the game, created with OpenGL
        It used PyGlet to bind OpenGL to Python
    """

    def __init__(self, game):
        """
            Constructor
        """
        #TODO: add these in arguments
        width = 200
        height = 200

        # Create the window
        self.factory = WindowFactory()
        self.factory.createLabel('Koridor', 0, 300)  # Title

        # Create the grid (by Kevin Flynn)
        self.grid = self.factory.createGrid(game.board, width, height)

        # Create players & walls
        self.players = game.players
        self.map = game.board.map
        self.refresh()

        # Add events
        self.on_draw = self.factory.window.event(self.on_draw)
        self.on_key_press = self.factory.window.event(self.on_key_press)
        self.on_mouse_press = self.factory.window.event(self.on_mouse_press)

        # Run Forest, run !
        pyglet.app.run()

        # Exit
        print('Thanks a lot for playing !')

    def refresh(self):
        """
            Method to refresh the interface
        """
        self.factory.removePlayers()
        for player in self.players:
            self.factory.createPlayer(player, self.grid)

    def on_draw(self):
        """
            Event to clear & draw the window
        """
        self.factory.draw()

    def on_key_press(self, symbol, modifiers):
        """
            Event to bind keys to actions
        """
        if symbol == key.Z or symbol == key.UP:
            print ('Go up.')
        elif symbol == key.D or symbol == key.RIGHT:
            print ('Go right.')
        elif symbol == key.S or symbol == key.DOWN:
            print ('Go down.')
        elif symbol == key.Q or symbol == key.LEFT:
            print ('Go left.')

    def on_mouse_press(self, x, y, button, modifiers):
        """
            Event to bind mouse to actions
        """
        if button == mouse.LEFT:
            coord = self.grid.getCaseByAbsolutCoordinates(x, y)
            if coord:
                print(coord)
