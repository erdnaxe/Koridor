# -*- coding: utf-8 -*-
"""This project consists of recreating the Koridor game in Python.
@author: Iooss
@license: MIT
"""

from game import *
from shellInterface import *
from action import *

game = Game()
interface = ShellInterface(game)

game.board.iterativCheckPath([0, 0], [[]])

while True:
    # Draw the grid
    interface.drawGrid()

    # Ask and play an action
    stringAction = interface.askAction()
    action = Action()
    if action.stringToAction(stringAction):
        # the action is valid
        if game.play(action):
            # End of the game
            if game.isFinished():
                print("Le joueur " + str(game.isFinished()) + " a gagné")
                game.newGame()
    else:
        # not a valid action
        print("Action inconnue")
