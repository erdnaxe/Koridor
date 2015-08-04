# -*- coding: utf-8 -*-
"""This project consists of recreating the Koridor game in Python.
@author: Iooss
@license: MIT
"""

from game import *
from shellInterface import *

game = Game()
interface = ShellInterface(game)

while True:
    # Draw the grid
    interface.drawGrid()

    # Ask and play an action
    game.play(interface.askAction())

    # End of the game
    if game.isFinished():
        print("Le joueur " + game.isFinished() + " a gagné")
        game.newGame()
