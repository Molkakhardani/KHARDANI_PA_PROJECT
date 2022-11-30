from player import Player
from game import Game


# 2D arrays to draw the players
player1Schema = [["<", "O", ">", " ", "\n"],
                 [" ", "|", "_", " ", "\n"],
                 [" ", "|", " ", "\\", "\n"],
                 [" ", "|", " ", " ", "\n"],
                 ["/", "|", " ", " ", "\n"],]

player2Schema = [[" ", "<", "O", ">", "\n",],
                 [" ", "_", "|", " ", "\n"],
                 ["/", " ", "|", " ", "\n"],
                 [" ", " ", "|", " ", "\n"],
                 [" ", " ", "|", "\\", "\n"],]


# check the main thread and run the game
if __name__ == "__main__":
    try:
        # prepare players instances with Player Class
        player1 = Player(player1Schema, 1)
        player2 = Player(player2Schema, 2)

        # instanciate the Game and enter a while loop
        game = Game(player1, player2)
        while game.main():
            pass
        # quit curses and print exception if there was an error
    except Exception as e:
        print(e)
