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
        # Getting all infos about the game
        self.game = game
        self.board = game.board
        self.players = game.players

        # Create the window
        self.factory = WindowFactory()
        self.factory.createLabel('Koridor', 0, 300)
        self.createGrid()

        # Add events
        self.on_draw = self.factory.window.event(self.on_draw)
        self.on_key_press = self.factory.window.event(self.on_key_press)
        self.on_mouse_press = self.factory.window.event(self.on_mouse_press)

        # Run Forest, run !
        pyglet.app.run()

        # Exit
        print('Thanks a lot for playing !')

    def createGrid(self):
        """
            Method to create objects to draw the grid
        """
        origin = [50, 50]
        size = 100

        self.factory.createLines(0, size, size, size, origin)  # top line
        self.factory.createLines(size, size, size, 0, origin)  # right line
        self.factory.createLines(size, 0, 0, 0, origin)  # bottom line
        self.factory.createLines(0, 0, 0, size, origin)  # left line

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
            print ('The left mouse button was pressed.')

    def drawGrid(self):
        """
            Method to draw the grid
        """
        print()  # new line

        for i in range(self.board.size):
            y = self.board.size - 1 - i
            print((self.horizontalGridLine(y)))

            if y != 0:
                # draw the bottom horizontal line of walls
                print((self.horizontalWalls(y)))

    def horizontalGridLine(self, y):
        """
            Method to return a horizontal line of vertical walls and players
        """
        tmpReturn = ''

        for x in range(self.board.size):
            tmpReturn += self.centerCase([x, y])

            # draw right wall
            if x != self.board.size - 1:
                tmpReturn += self.verticalWall(self.board.map[x][y])

        return tmpReturn

    def centerCase(self, position):
        """
            Method to return the center of a case
        """
        playerId = self.getPlayerByPosition(position)
        if playerId != 0:
            return ' ' + str(playerId)
        else:
            return '  '

    def verticalWall(self, case):
        """
            Method to return the wall between 2 players
        """
        if case.hasWall(2):
            return '█'
        else:
            return '│'

    def horizontalWalls(self, y):
        """
            Method to return a horizontal line of walls (not the player line)
        """
        tmpReturn = ''

        for x in range(self.board.size):
            if self.board.map[x][y].hasWall(3):
                tmpReturn += '■■'
            else:
                tmpReturn += '——'

            # Draw the plus
            if x != self.board.size - 1:
                tmpReturn += '┼'

        return tmpReturn

    def getPlayerByPosition(self, position):
        """
            return le joueur correspondant a la position
        """
        for player in self.players:
            if player.position == position:
                return player.id
        return 0