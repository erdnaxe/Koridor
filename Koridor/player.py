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
            self.initPosition = [4, 0]
            self.position = [4, 0]
        elif self.id == 2:
            self.initPosition = [4, 8]
            self.position = [4, 8]
        else:
            print("This software doesn't support more than 2 players.")

    def executeAction(self, action, board):
        """
            Take an object Action and execute it
        """
        for i in range(1, 5):
            if action.id == i:
                # check the wall
                if not board.map[self.position[0]][self.position[1]].hasWall(i):
                    self.move(i)
                    return True

        return False

    def move(self, idDeplacement):
        """
            Change the position of the player depending of the id of the
            deplacement
        """
        if idDeplacement == 1:
            self.position = [self.position[0], self.position[1] + 1]
        elif idDeplacement == 2:
            self.position = [self.position[0] + 1, self.position[1]]
        elif idDeplacement == 3:
            self.position = [self.position[0], self.position[1] - 1]
        elif idDeplacement == 4:
            self.position = [self.position[0] - 1, self.position[1]]

        return
