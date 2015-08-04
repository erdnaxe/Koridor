# -*- coding: utf-8 -*-
"""This is the Case class.
@author: Iooss
@license: MIT
"""


class Case:
    idClass = 1

    def __init__(self):
        self.id = Case.idClass
        Case.idClass += 1

        self.walls = 4 * [False]
        self.player = None

    def placeWall(self, coords, side):
        """
            Method to place a wall in this case
            The attribute side takes values from 1 to 4
            1 => top,
            2 => left,
            3 => bottom,
            4 => right

            Exemple:
                placeWall(coords = [0, 0], side = 4)
        """
        self.walls[side] = True
