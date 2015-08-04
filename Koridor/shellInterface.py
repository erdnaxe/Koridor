# -*- coding: utf-8 -*-
"""This is the ShellInterface class. With this class,
you can draw a Koridor game in a monospace Shell.
@author: Iooss
@license: MIT
"""


class ShellInterface:

    def __init__(self, game):
        self.board = game.board
        self.players = game.players

    def drawGrid(self):
        """
            Method to draw the grid
        """
        print()  # new line
        for x in range(self.board.size):
            for y in range(self.board.size):
                self.drawMiddleCase([x, y])
                if y != self.board.size - 1:
                    self.drawVerticalWall(x, y)
                else:
                    print()  # new line
                    self.drawHorizontalWalls(x)

    def drawVerticalWall(self, x, y):
        """
            Method to draw the wall between 2 players
        """
        if self.board.map[x][y].hasWall(2):
            print('█', end='')
        else:
            print('|', end='')

    def drawHorizontalWalls(self, x):
        """
            Method to draw a horizontal line of walls (not the player line)
        """
        if x != self.board.size - 1:
            for y in range(self.board.size):
                if self.board.map[x][y].hasWall(1):
                    print('■■', end='')
                else:
                    print('--', end='')

                # Draw the plus
                if y != self.board.size - 1:
                    print('+', end='')
            print()  # new line

    def drawMiddleCase(self, position):
        """
            Method to draw the center of a case (with the player if he is here)
        """
        playerId = self.board.getPlayerByPosition(position)
        if playerId != 0:
            print(str(playerId) + ' ', end='')
        else:
            print('  ', end='')

    def askAction(self):
        print("What must I do ?")
        return input("> ")
