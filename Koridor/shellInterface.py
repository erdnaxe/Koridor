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
        self.players = game.players

    def drawGrid(self):
        """
            Method to draw the grid
        """
        self.positionsUsed = []
        self.positionsPlayers = {}
        for player in self.players:
            self.positionsUsed.append(player.position)
            self.positionsPlayers[player.position] = player

        print()  # new line
        for x in range(self.size):
            for y in range(self.size):
                self.drawMiddleCase([x, y])
                if y != self.size - 1:
                    self.drawVerticalWall(x, y)
                else:
                    print()  # new line
                    self.drawHorizontalWalls(x)

    def drawVerticalWall(self, x, y):
        """
            Method to draw the wall between 2 players
        """
        if self.map[x][y].hasWall(2):
            print('█', end='')
        else:
            print('|', end='')

    def drawHorizontalWalls(self, x):
        """
            Method to draw a horizontal line of walls (not the player line)
        """
        if x != self.size - 1:
            for y in range(self.size):
                if self.map[x][y].hasWall(1):
                    print('■■', end='')
                else:
                    print('--', end='')

                # Draw the plus
                if y != self.size - 1:
                    print('+', end='')
            print()  # new line

    def drawMiddleCase(self, position):
        """
            Method to draw the center of a case (with the player if he is here)
        """
        if position in positionsUsed:
            print(str(self.positionsPlayers[position].id) + ' ', end='')
        else:
            print('  ', end='')

    def askAction(self):
        print("What must I do ?")
        return input("> ")
