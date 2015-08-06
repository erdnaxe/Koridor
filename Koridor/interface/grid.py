# -*- coding: utf-8 -*-
from .lines import *


class Grid():
    """
        Class to create objects to draw the grid
    """

    def __init__(self, size_x, size_y, width, height):
        """
            Constructor
        """
        self.size_x = size_x
        self.size_y = size_y
        self.width = width
        self.height = height

        self.recalculate()

    def recalculate(self):
        """
            Method to refresh the grid
        """
        # Remove all items
        self.items = []

        origin = [50, 50]

        self.items += [Lines(0, self.height, self.width, self.height, origin)]
        self.items += [Lines(self.width, self.height, self.width, 0, origin)]
        self.items += [Lines(self.width, 0, 0, 0, origin)]
        self.items += [Lines(0, 0, 0, self.height, origin)]

    def draw(self):
        """
            Draw the grid
        """
        for item in self.items:
            item.draw()

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