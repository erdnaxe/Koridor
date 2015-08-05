# -*- coding: utf-8 -*-
"""This is the ShellInterface class. With this class,
you can draw a Koridor game in a monospace Shell.
@author: Iooss
@license: MIT
"""


class ShellInterface:
    """
        With the ShellInterface you can draw a Koridor game in a
        monospace Shell. It uses ascii box characters.
    """

    def __init__(self, game):
        """
            Constructor
        """
        self.board = game.board
        self.game = game

    def drawGrid(self):
        """
            Method to draw the grid
        """
        print()  # new line

        for x in range(self.board.size):
            print((self.horizontalGridLine(x)))

            if x != self.board.size - 1:
                # draw the bottom horizontal line of walls
                print((self.horizontalWalls(self.board.map[x])))

    def horizontalGridLine(self, x):
        """
            Method to return a horizontal line of vertical walls and players
        """
        tmpReturn = ''

        for y in range(self.board.size):
            tmpReturn += self.centerCase([x, y])
            if y != self.board.size - 1:
                # draw right wall
                tmpReturn += self.verticalWall(self.board.map[x][y])

        return tmpReturn

    def centerCase(self, position):
        """
            Method to return the center of a case
        """
        playerId = self.board.getPlayerByPosition(position)
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

    def horizontalWalls(self, line):
        """
            Method to return a horizontal line of walls (not the player line)
        """
        tmpReturn = ''

        for y in range(self.board.size):
            if line[y].hasWall(1):
                tmpReturn += '■■'
            else:
                tmpReturn += '——'

            # Draw the plus
            if y != self.board.size - 1:
                tmpReturn += '┼'

        return tmpReturn

    def askAction(self):
        """
            Ask the user the action he wants to execute
        """
        print(("C'est au joueur " + str(self.game.activePlayer + 1)
            + " de jouer."))
        command = str(input("> "))
        return command
