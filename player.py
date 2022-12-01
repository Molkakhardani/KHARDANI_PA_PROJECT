import numpy as np


class Player:
    def __init__(self, schema, number):
        # a sechma is 2D array
        self.schema = schema

        # keep track of the firstPlayer number of steps
        self.firstPlayerSteps = 0
        self.secondPlayerSteps = 0

        # keep the instanciated player number
        self.playerNumber = number

    # return the upated player schema
    def getPlayerData(self):
        return self.schema

    # attack function and change the sword cell only
    def attack(self):
        if (self.playerNumber == 1):
            self.schema[2][self.firstPlayerSteps + 3] = " "
            self.schema[1][self.firstPlayerSteps + 3] = "__"
        if (self.playerNumber == 2):
            self.schema[2][self.secondPlayerSteps] = " "
            self.schema[1][self.secondPlayerSteps] = "__"

    # rest mode
    def rest(self):
        if (self.playerNumber == 1):
            self.schema[1][self.firstPlayerSteps + 3] = " "
            self.schema[2][self.firstPlayerSteps + 3] = "\\"
        if (self.playerNumber == 2):
            self.schema[1][self.secondPlayerSteps] = " "
            self.schema[2][self.secondPlayerSteps] = "/"

    # block function and change the shield cell only
    def block(self):

        if (self.playerNumber == 1):
            self.schema[1][self.firstPlayerSteps + 3] = "]"
            self.schema[2][self.firstPlayerSteps + 3] = " "
        if (self.playerNumber == 2):
            self.schema[1][self.secondPlayerSteps] = "["
            self.schema[2][self.secondPlayerSteps] = " "

    # moveForward function => add empty cells at the beginning of each sub array.
    def moveForward(self):
        # check to not get out of the screen
        if (self.playerNumber == 1 and self.firstPlayerSteps < 15):
            for i in range(len(self.schema)):
                self.schema[i].insert(0, " ")
            self.firstPlayerSteps += 1
        # check to not get out of the screen
        if (self.playerNumber == 2 and 0 <= self.secondPlayerSteps < 15):
            for i in range(len(self.schema)):
                self.schema[i].insert(0, " ")
            self.secondPlayerSteps += 1
   

    # moveBackward function => remove empty cells from the beginning of each sub array.
    # keep track of the position with the number of steps (firstPlayerSteps)
    def moveBackward(self):
        # check to not get out of the screen
        if ((self.playerNumber == 1 and self.firstPlayerSteps > 0)):
            for i in range(len(self.schema)):
                self.schema[i].pop(0)
            if (self.playerNumber == 1):
                self.firstPlayerSteps -= 1

        # check to not get out of the screen
        if ((self.playerNumber == 2 and self.secondPlayerSteps > 0)):
            for i in range(len(self.schema)):
                self.schema[i].pop(0)
            if (self.playerNumber == 2):
                self.secondPlayerSteps -= 1  