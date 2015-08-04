# -*- coding: utf-8 -*-


class Action:
    """
        This class create an object to encode the player wish of action
    """
    def __init__(self):
        """
            constructor
        """
        self.action = ""
        self.wallCoordinate = [0,0]
        self.wallType = 0
        # 1 : le mur commence en haut et s'etend a gauche
        # 2 : le mur commence a droite et

    def stringToAction(self, actionSring):
        """
            This method take a string and init the Action object depending of it
        """

