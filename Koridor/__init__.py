# -*- coding: utf-8 -*-
"""This project consists of recreating the Koridor game in Python.
@author: Iooss
@license: MIT
"""

from game import *


game = Game()

while True:
    #demande pour action
    print("que faire ?")
    action = input("> ")

    game.play(action)

    # affiche jeu

    if game.isFinished():
        print("Le joueur " + game.isFinished() + " a gagné")
        game.newGame()
