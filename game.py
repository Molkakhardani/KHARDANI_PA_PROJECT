import curses
import keyboard
import numpy as np
import time 


class Game:
    def __init__(self, player1, player2):

        # set display size
        self.width = 22
        self.height = 17

        # prepare the two players Objects
        self.player1 = player1
        self.player2 = player2

        # prepare the two players data (2D array) that will be printed by the game class
        self.player1Data = player1.getPlayerData()
        self.player2Data = player2.getPlayerData()
        # set up curses
        self.setupCurses()

    def main(self):
        # prepare three different windows (board/ player1 / player2)
        self.prepareBattleGame()

        # print the score board
        self.printBoard()
        # print the first player with the data and the associated screen
        self.printPlayer(self.player1Data, self.playerOneScreen)
        # print the second player with the data and the associated screen
        self.printPlayer(self.player2Data, self.playerTwoScreen)

        while True:
            start_time =time.time()
            x=1
            counter=0

            # catch all the keyboard event
            event = keyboard.read_event()
            if (event.event_type == keyboard.KEY_DOWN):
                # first player controls
                if (event.name == 'z'):
                    self.player1.attack()
                if (event.name == 'd'):
                    self.player1.moveForward()
                if (event.name == 'q'):
                    self.player1.moveBackward()
                if (event.name == 's'):
                    self.player1.block()

                # second player controls
                if (event.name == 'o'):
                    self.player2.attack()
                if (event.name == 'p'):
                    self.player2.block()
                if (event.name == 'droite'):
                    self.player2.moveForward()
                if (event.name == 'gauche'):
                    self.player2.moveBackward()

            # each time the key up we have to reset the display and put the player in rest (\).
            if (event.event_type == keyboard.KEY_UP):
                # put the player in rest mode
                self.player1.rest()
                self.player2.rest()

            # get the new data schema from each player instance after updating it
            self.updateFirstPlayerMovement(
                self.player1.getPlayerData())
            self.updateSecondPlayerMovement(
                self.player2.getPlayerData())

            # calculate the FPS after each event
            # https://stackoverflow.com/questions/43761004/fps-how-to-divide-count-by-time-function-to-determine-fps
            counter+=1
            if (time.time()- start_time)> x:
                FPS = counter/(time.time()- start_time)
                counter=0
                start_time =time.time()
                time.sleep(FPS)


    def prepareBattleGame(self):

        # calculate where to place main window
        windowWidth = self.width * 2
        self.windowStart = int(round(self.cols/2) - round(windowWidth/2))

        # prepare score display
        self.scoreDisplay = curses.newwin(
            1, self.width*2+2, 0, self.windowStart)

        # prepare the first player screen
        self.playerOneScreen = curses.newwin(
            10, self.width, 15, 1)

        # prepare the second player screen
        self.playerTwoScreen = curses.newwin(
            10, self.width, 15, 20)

    # function to set up curses
    def setupCurses(self):

        # configure curses
        self.screen = curses.initscr()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        curses.curs_set(0)  # make cursor invisible
        curses.cbreak()
        curses.noecho()  # prevents user input from being echoed

        # get size of screen
        self.rows, self.cols = self.screen.getmaxyx()

    # print the score borad on the top of the battle in the middle of the screen
    def printBoard(self):
        # refresh score display (static values)
        self.scoreDisplay.addstr(0, 0, "| 1 | Ø |")
        self.scoreDisplay.refresh()

    # a function that iterates over 2D array in order to display the player last updated schema
    def printPlayer(self, palyerData, playerScreen):
        # delete the old player displayed data on the terminal
        playerScreen.clear()
        for i in range(len(np.array(palyerData))):
            for j in range(len(np.array(palyerData)[i])):
                if (np.array(palyerData)[i][j] == "__"):
                    # Red Color for sword only
                    playerScreen.addstr(
                        i, j, np.array(palyerData)[i][j], curses.color_pair(1))
                else:
                    playerScreen.addstr(
                        i, j, np.array(palyerData)[i][j])
        # refesh with the new data
        playerScreen.refresh()

    def updateFirstPlayerMovement(self, updatedPlayerData):
        self.printPlayer(updatedPlayerData, self.playerOneScreen)

    def updateSecondPlayerMovement(self, updatedPlayerData):
        self.printPlayer(updatedPlayerData, self.playerTwoScreen)
