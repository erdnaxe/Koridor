# -*- coding: utf-8 -*-


class Case:
    idClass = 1

    def __init__(self):
        self.id = Case.idClass
        Case.idClass += 1

        self.walls = 4 * [0]  # 1 : haut, 2 : droite, 3 : bas, 4 : gauche
        self.player = None
