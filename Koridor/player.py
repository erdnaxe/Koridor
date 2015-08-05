# -*- coding: utf-8 -*-



class Player:
    """
        this class implement the player
    """
    idClass = 1

    def __init__(self):
        """
            constructor
        """
        self.id = Player.idClass
        Player.idClass += 1

        self.walls = 10
        self.initPosition = []
        self.position = []

        if self.id == 1:
            self.initPosition = [0, 4]
            self.position = [0, 4]
        elif self.id == 2:
            self.initPosition = [8, 4]
            self.position = [8, 4]
        else:
            print("This software doesn't support more than 2 players.")

    def executeAction(self, action, board):
        """
            Take an object Action and execute it
        """
        if action.id == 1:  # forward
            # check the wall
            if not board.map[self.position[0]][self.position[1]].hasWall(1):
                self.position = [self.position[0], self.position[1] + 1]




        return False
