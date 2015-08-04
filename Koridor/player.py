# -*- coding: utf-8 -*-


class Player:
    idClass = 1

    def __init__(self):
        self.id = Player.idClass
        Player.idClass += 1

        self.walls = 10

        if self.id == 1:
            self.initposition = [0, 4]
            self.position = [0, 4]
        elif self.id == 2:
            self.initposition = [8, 4]
            self.position = [8, 4]
        else:
            print("This software doesn't support more than 2 players. Sorry, go make yourself a coffee.")  # To DO (not the coffee)
