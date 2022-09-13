from game_board import MastermindBoard
from datetime import datetime

def main():
    """takes the mastermindboard class and calls the main function that is able
    to process everything and build the play and play the game. This allows for
    a small main and and a small file that is just needed to run the game. 
    """
    gameboard = None
    try:
        # MastermindBoard class to contain everything needed to make the 
        # gameboard and run the game
        gameboard = MastermindBoard()
        # runs the game
        gameboard.run_mastermind_game()
    # file not found error
    except FileNotFoundError as error:
        # prints an error pop up message
        gameboard.add_gifs('file_error.gif')
        # writes down the errors in a file
        with open('mastermind_errors.err', "a") as errorfile:
            errorfile.write(str(datetime.now()))
            errorfile.write(str((error)))
            errorfile.write("\n")
    # any other errors that are noticed
    except Exception as error:
        # writes down the errors in a file
        with open('mastermind_errors.err', "a") as errorfile:
            errorfile.write(str(datetime.now()))
            errorfile.write(str((error)))
            errorfile.write("\n")
    return True      
if __name__ == "__main__":
    main()