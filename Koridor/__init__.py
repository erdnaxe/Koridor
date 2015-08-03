# -*- coding: utf-8 -*-
from game import *


game = Game()

while True:
    #demande pour action
    print("que faire ?")
    action = input("> ")

    game.play()

    # affiche jeu

    if game.isFinished():
        print("Le joueur " + game.isFinished() + " a gagné")
        game.newGame()
