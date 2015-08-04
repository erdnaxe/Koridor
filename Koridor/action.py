# -*- coding: utf-8 -*-


class Action:
    """
        This class create an object to encode the player wish of action
    """
    allActions = ["go_forward", "go_backward", "go_left",
                "go_right", "place_wall"]

    def __init__(self):
        """
            constructor
        """
        self.action = ""
        self.wallCoordinate = [0, 0]
        self.wallType = 0
        # 1 : le mur commence en haut et s'etend a gauche
        # 2 : le mur commence a droite et s'etend en bas
        # 3 : le mur commence en bas et s'etend a gauche
        # 4 : le mur commence a geuche et s'etend en bas'

    def stringToAction(self, actionSring):
        """
            This method take a string and init the Action object depending of it
        """
        if actionSring in Action.allActions[:4]:
            self.action = actionSring
            return True
        elif actionSring in Action.allActions[4]:
            # cas du placement de mur
            return True
