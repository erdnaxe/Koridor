# -*- coding: utf-8 -*-


class Player:
    idClass = 1

    def __init__(self):
        self.id = Player.idClass
        Player.idClass += 1

        self.walls = 10