# mastermind-board-game
The project design includes 5 python files along with a bunch of gif files
in order to build and play on the proper gameboard for mastermind. In gameboard
it holds multiple functions that for instance draw different parts of the 
gameboard, put new highscores in a file and draw them on the gameboard, make
clickable marbles and objects, allow the player to click objects including a 
checkbutton to confirm guesses and an xbutton to remove guesses along with a 
quit button. Each function is designed in order to make each of these important 
aspects in their own function and is called whenever needed. In order to make 
the play file as minimal as possible the gameboard is designed in game_board 
and mastermind_game only holdsthe function needed to run it all including 
writing any errors that are to take place.
    Overall, this design was used to maximize function use by writing little
amounts of code in each and using them to each handle specific task and using
one function to store all the little ones to draw and run the game.
