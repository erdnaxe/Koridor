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

    def askAction(self):
        """
            Ask the user the action he wants to execute
        """
        print(("C'est au joueur " + str(self.game.activePlayer + 1)
            + " de jouer."))
        command = str(input("> "))
        return command
