# -*- coding: utf-8 -*-
"""This is the ShellInterface class. With this class,
you can draw a Koridor game in a monospace Shell.
@author: Iooss
@license: MIT
"""


class ShellInterface:

    def __init__(self, game):
        self.size = game.board.size
        self.map = game.board.map

    def drawGrid(self):
        for x in range(self.size):
            for y in range(self.size):
                self.drawLeftRightWall(x, y, 4)
                self.drawMiddleCase(x, y)
                if y == self.size - 1:
                    self.drawLeftRightWall(x, y, 2)
                    print('')  # newline

    def drawLeftRightWall(self, x, y, side):
        if self.map[x][y].hasWall(side):
            print('||', end='')
        else:
            print('██', end='')

    def drawMiddleCase(self, x, y):
        if self.map[x][y].player is None:
            print('  ', end='')
        else:
            print(str(self.map[x][y].player.id), end='')
