from Marble import Marble
from Point import Point
from typing import List
from datetime import datetime
import os
import turtle 
import time
import random

# used to switch the direction of the turtle 90 degrees
TURN_RIGHT = 90

class MastermindBoard():
    def __init__(self, color="blue", line_thickness=10):
        """a construtor which is used to initialize/assign values to all the 
        data of the class when and object of class is created.

        Args:
            color (str): makes the leaderboard outline blue. 
            Defaults to "blue".
            line_thickness (int): makes the turtle pen thicker in order to 
            make a thicker outline for the gameboard squares. Defaults to 10.
        """
        # creates a new pen
        self.pen = self.new_pen()
        # change the color for the leaderboard outline
        self.color = color
        # change the line thickness to be bolder
        self.line_thickness = line_thickness
        # set a default variable for the screen
        self.window = turtle.Screen()
        # set screen to a default size for every computer it opens on
        self.window.setup(width=1000, height=600)
        # fastest speed
        self.pen.speed(0)
        # hide the turtle to make it go fastest
        self.pen.hideturtle()
        # make each of the different marbles stored inside lists
        self.big_marbles: List[List[Marble]] = []
        self.small_marbles: List[List[Marble]] = []
        self.colored_marbles: List[Marble] = []
        # store all the colored marbles needed for the game
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        # be able to handle clicks on the screen when needed
        turtle.onscreenclick(self.handle_button_clicks)
        # current row of marbles
        self.current_row = 0
        # make check button a marble in order to click on it
        self.check_button: Marble = None
        # make x button a marble in order to click on it
        self.x_button: Marble = None
        
    def get_user(self):
        """gets the players username which they are able to type in whatever
        they want to use."""
        # title for turtle window
        turtle.title("CS5001 MasterMind Code Game")
        # obtain the users name in order to display them on a leaderboard
        # after they play and if they win
        self.username = turtle.textinput("CS5001 Mastermind", "Your Name:")
         
    def new_pen(self) -> turtle: 
        """generates a new pen

        Returns:
            turtle: generates a new turtle to work with
        """
        return turtle.Turtle()
    
    def draw_rectangle(self, width: int, height: int):
        """whenever called makes a rectangle for the gameboard and has 
        whatever objects needed placed inside.
        
        Args:
            width (int): the width of the rectangle passed in
            height (int): the height of the rectangle passed in
        """
        self.pen.forward(width)
        # turn right is a global constant which is equal to 90
        self.pen.right(TURN_RIGHT)
        self.pen.forward(height)
        self.pen.right(TURN_RIGHT)
        self.pen.forward(width)
        self.pen.right(TURN_RIGHT)
        self.pen.forward(height)
        self.pen.right(TURN_RIGHT)
        
    def draw_gameboard(self, width: int, height: int):
        """makes the initial rectangle that will eventually have the big and
        small marbles drawn inside.

        Args:
            width (int): the width of the rectangle passed in
            height (int): the height of the rectangle passed in
        """
        # draw the gameboard rectangle
        # makes the pensize bigger for a thicker border
        self.pen.pensize(self.line_thickness)
        self.pen.penup()
        self.pen.goto(-480,430)
        self.pen.pendown()
        # calls the function in order to make a rectangle for the gameboard
        self.draw_rectangle(width, height)
        
    def draw_leaderboard(self, width: int, height: int):
        """makes the blue rectangle which will eventually have the leaderboard
        scores and names drawn inside.

        Args:
            width (int): the width of the rectangle passed in
            height (int): the height of the rectangle passed in
        """
        # draw the leaderboard rectangle
        # makes the pensize for the border thickness
        self.pen.pensize(8)
        # sets pen color to blue
        self.pen.color(self.color)
        self.pen.penup()
        self.pen.goto(220, 430)
        self.pen.pendown()
        # calls the function in order to make a rectangle for the gameboard
        self.draw_rectangle(width, height)
    
    def draw_high_score_header(self):
        """writes leaders at the top of the blue rectangle made in order to 
        display previous players and their score.
        """
        self.pen.pensize(8)
        # set pen color to blue
        self.pen.color(self.color)
        self.pen.penup()
        self.pen.goto(250, 375)
        # writes this at the top of the leaderboard rectangle
        self.pen.write("Leaders: ", font=("Calibri", 20, "bold"))
        self.pen.pendown()
        
    def hold_game_clickables(self, width, height):
        """makes the rectangle that eventually surrounds all the game objects 
        that are going drawn and going to be clicked in order to play the game. 
        
        Args:
             width (int): the width of the rectangle passed in
            height (int): the height of the rectangle passed in
        """
        # draw the game objects box needed to surround the 
        # clickable marbles/clickable buttons
        # set pen from blue to black
        self.pen.color("black")
        # makes the pensize bigger for a thicker border
        self.pen.pensize(self.line_thickness)
        self.pen.penup()
        self.pen.goto(-480, -275)
        self.pen.pendown()
        # calls the function in order to make a rectangle for the gameboard
        self.draw_rectangle(width, height)
        
    def add_gifs(self, name_of_gif, x: int, y: int): 
        """places down any gif/pictures needed in order to have a distinguished
        quit button, confirm guesses, remove guesses button along with any
        errors that present themselves and win/lose gifs.

        Args:
            name_of_gif (str): name of gif file being added 
            x (int): x coordinate gif is being placed
            y (int): y coordinate gif is being placed
        """
        # showturtle() in order to make it visible to show gifs
        self.pen.showturtle()
        try:
            # .addshape() adds a gif
            self.window.addshape(name_of_gif)
        except Exception:
            raise FileNotFoundError
        self.pen.up()
        # go to the coordinates for the gif to be placed
        self.pen.goto(x, y)
        # gets the name of the gif needed to be placed
        self.pen.shape(name_of_gif)
        # leaves the gif at the spot it needs to go
        self.pen.stamp()
        self.pen.down()
        # "blank" in order to reset the pen and have no shape on it
        self.pen.shape("blank")
        
    def gifs(self):
        """holds gifs and their specific coordinates needed to be placed at
        also any gifs that need to be clicked on and are marble shaped are made
        into a marble object.
        """
        # checkbutton gif for confirming guesses after 4 are made
        self.add_gifs('checkbutton.gif', 60, -340)
        # draw a marble in order to make it clickable
        self.check_button = Marble(Point(60, -370), "white", size = 30)
        # quit gif in order to quit the game
        self.add_gifs('quit.gif', 325, -350)
        # draw a marble in order to make it clickable 
        self.x_button = Marble(Point(160, -370), "white", size = 30)
        # xbutton gif in order to remove any guesses not wanted
        self.add_gifs('xbutton.gif', 160, -340)
               
    def draw_empty_marbles(self):
        """makes the big and small marbles that are intiatlly placed on the 
        gameboard and each of the rows of marbles are stored in a list meaning
        the big marbles of stored in lists of 4 and eventually in one big list
        and the small marbles are stored in 2 rows of 2 and eventually stored
        in one big list.
        """
        # creates rows of 4 big marbles
        
        # starting y point
        current_y = 410
        # 10 rows
        for y in range(10):
            # forms a list for each row
            row = []
            # starting x point
            current_x = -450
            # subtracts y in order to make a different row
            current_y  = current_y - 63
            # create 4 in a row
            for x in range(4):
                # adds x in order to keep same row but different place
                current_x = current_x + 70
                # in order to create each marble object at a specific 
                # coordinate, size and color
                marble = Marble(Point(current_x, current_y), "white", size=23)
                # draw empty marbles
                marble.draw_empty()
                # adds the marble to an existing list
                row.append(marble)
            # eventually stores all the big marbles in one list based off each
            # row of 4
            self.big_marbles.append(row)       
        
        # creates rows of 2 small marbles
        
        # starting y point
        current_y = 390
        # forms a list for each row
        row = []
        # 20 rows
        for y in range(20):
            # starting x point
            current_x = -50
            # mod to make 2 rows of 2 close to each other then separate further
            # apart and create mini squares of marbles 
            if y != 0 and y % 2 == 0:
                row = []
                current_y = current_y - 48
            else:
                current_y = current_y - 15
            # create 2 in a row
            for x in range(2): 
                # adds x in order to keep same row but different place
                current_x = current_x + 20 
                # in order to create each marble object at a specific 
                # coordinate, size and color
                marble = Marble(Point(current_x, current_y), "white", size=5)
                # draw empty marbles 
                marble.draw_empty()
                # adds the marble to an existing list
                row.append(marble)
            if y != 0 and y % 2 == 1:
                # eventually stores all the big marbles in one list based off 
                # each 2 rows of 2
                self.small_marbles.append(row)
            
    def draw_colored_marbles(self):
        """make the colored marbles at the bottom in order for the player 
        to click on in order to start guessing the correct pattern the ai
        has intended.
        """
        # make the colored marbles in order for the player to start guessing
        color = self.colors
        # current x,y to have the colored marbles placed correctly at the 
        # bottom for the player to click on and guess the pattern
        current_y = -360
        current_x = -490
        # for loop to have each colored filled in the 6 marbles at the bottom
        for colors in color:
            current_x = current_x + 75 
            # in order to create each marble object at a specific 
                # coordinate, size and color  
            marble = Marble(Point(current_x, current_y), colors, size=27)
            # draw empty marbles
            marble.draw_empty()
            # fill the marbles with the colors
            marble.draw()   
            # store the colored marbles in a list
            self.colored_marbles.append(marble)
    
    def make_a_random_color_code(self) -> list:
        """makes a randomized color code of the 6 colors.

        Returns:
            list: returns a list of the colored marbles
        """
        self.secret_code = random.sample(self.colored_marbles, k=4)
       
        return self.secret_code
    
    def check_if_color_in_color_code(self, marble: Marble) -> bool:
        """checks if the color is inside the secret code so the small marbles
        can be filled with the color red.

        Args:
            marble (Marble): marble object
        Returns:
            bool: returns true or false
        """
        secret_code_colors = [x.get_color() for x in self.secret_code]
        is_in_secret_code = marble.get_color() in secret_code_colors
        
        return is_in_secret_code
    
    def handle_button_clicks(self, x: int, y: int):
        """handles the button clicks for checking to see if the colored marbles
        were clicked, confirming guesses the player clicked, removing guesses 
        and if the quit button was clicked.

        Args:
            x (int): x coordinate to check if it was clicked_in_region
            y (int): y coordinate to check if it was clicked_in_region
        """
        # if the quit button is clicked exit the game 
        if x > 225 and x < 424 and y > -405 and y < -294:
            # add the quit message
            self.add_gifs('quitmsg.gif', 0, 0)
            # sleep for 5 seconds then quit
            time.sleep(5)
            # exit the program
            turtle.bye()
        # check to see if colored marble was clicked
        self.check_if_marble_was_clicked(x, y)
        # confirm the 4 guesses of a row
        self.confirm_guesses(x, y)
        # remove guesses from a row 
        self.remove_guesses(x, y)
        
    def confirm_guesses(self, x: int, y: int):
        """allows the check button to be clicked and locks in guesses, checks
        to see if the colors from the users guesses are inside the secret code
        but wrong spot, if the colors are in the correct spot and correct color
        or if the color is not in the secret code. Also updates the leaderboard
        with however many rows it took to guess correctly.

        Args:
            x (int): x coordinate to check if it was clicked_in_region
            y (int): y coordinate to check if it was clicked_in_region
        """
        # if all the marbles aren't filled, not allowed to go to new row
        for big_marbles in self.big_marbles[self.current_row]:
            #if a big marble is empty in a row not allowed to move on
            if big_marbles.is_empty:
                return

        # calls click_in_region function to see if the insider of
        # the marble was clicked
        if self.check_button.clicked_in_region(x, y):
            for colored_marbles in self.colored_marbles:
                # draw colored marble
                colored_marbles.draw()

            num_correct = 0
            small_marble_colors = []
            
            for index, _ in enumerate(self.small_marbles[self.current_row]):
                # checks to see if there is a color present in the correct spot
                # and correct color making the first small marble available 
                # filled in black
                if self.secret_code[index].get_color() == self.big_marbles \
                [self.current_row][index].get_color():
                    small_marble_colors.append("black")
                    # adds one in order to check if num_correct equals 4 the 
                    # player wins
                    num_correct += 1
                # checks to see if there is a color present from the secret 
                # code in the guesses but in the wrong spot
                elif self.check_if_color_in_color_code(
                    self.big_marbles[self.current_row][index]):
                    small_marble_colors.append("red")
                else:
                    # if no color is present
                    small_marble_colors.append("white")
            
            # sort the small marbles in order to have black take the first 
            # open spots, red take the second spots, then white so the player
            # knows that there are correct colors but doesnt know which ones
            small_marble_colors = sorted(small_marble_colors, key=None, 
                                         reverse=False)
            
            # https://www.programiz.com/python-programming/methods/built-in/zip
            # idea for using zip in order to take iterables and form a tuple
            # since the small marbles need both the color which is a string
            # and the place in the row which is an integer
            for small_marble_color, small_marble in zip(
                small_marble_colors, self.small_marbles[self.current_row]):
                small_marble.set_color(small_marble_color)
                small_marble.draw()
                
            # if the player has 4 black filled small marbles, the player wins!
            if num_correct == 4:
                # add a winner gif
                self.add_gifs('winner.gif', 0, 0)
                
                
                
                # updates the leaderboard with the amount of rows it took
                # for the player to get the correct secret code and their
                # username acquired at the beginning
                guesses = str(self.current_row + 1)
                lines = []
                #https://pythonguides.com/file-does-not-exist-python/
                # got my idea for using os here. helped determine whether or 
                # not the leaderboard file exists and if it did then read it
                if os.path.exists("Leaderboard.txt"):
                    with open('Leaderboard.txt', "r") as leaderboard_info:
                    
                        for line in leaderboard_info:
                            lines.append(line.strip())
                # takes the amount of rows needed to get the correct code
                # and the username and writes it inside the file
                lines.append(guesses + " : " + self.username)
                # sorts the file by best score to worst (lowest score is at
                # the top)
                lines = sorted(lines, key=lambda x: 
                    x.partition(':')[0], reverse=False)
                # only writes 7 scores for the leaderboard
                lines = lines[0:7]
                # writes a new leaderboard file with the updated scores
                with open('Leaderboard.txt', "w") as leaderboard_info:
                    leaderboard_info.write("\n".join(lines))
                
                # sleep for 5 seconds then quit
                time.sleep(3)
                # exit the program
                turtle.bye()
            
            # lose if the player surpasses the 10 rows they have to guess
            elif self.current_row >= len(self.big_marbles) - 1:
                # adds a lose gif
                self.add_gifs('Lose.gif', 0, 0)
                # sleep for 3 seconds then quit
                time.sleep(3)
                
                self.pen.penup()
                self.pen.goto(-200, 300)
                # gives the player the correct code at the end in a pop up
                secret_code_colors = [x.get_color() for x in self.secret_code]
                code = " ".join(secret_code_colors)
                # display the secret code at the end
                turtle.textinput("Secret Code", code)
                self.pen.pendown()
                
                # sleep for 5 seconds then quit
                time.sleep(5)
                # exit the program
                turtle.bye()
                
            self.current_row += 1 
               
    def remove_guesses(self, x: int, y: int):
        """removes guesses when the player clicks the x button.

        Args:
            x (int): x coordinate to check if it was clicked_in_region
            y (int): y coordinate to check if it was clicked_in_region
        """
        # checks to see if the x button was clicked from the marble made 
        # surrounding it
        # resets all the big, small and colored marbles in the designated rows
        # that the player was guessing in at the time
        if self.x_button.clicked_in_region(x,y):
            for big_marbles in self.big_marbles[self.current_row]:
                # resets by drawing empty marbles
                big_marbles.draw_empty()
            for colored_marbles in self.colored_marbles:
                # redraws the colored marbles
                colored_marbles.draw()
            
    def check_if_marble_was_clicked(self, x: int, y: int):
        """checks to see if the colored marbles were clicked in order to put 
        them in the first big marble that is open at whatever row the player
        is on.

        Args:
            x (int): x coordinate to check if it was clicked_in_region
            y (int): y coordinate to check if it was clicked_in_region
        """
        color = None
        
        # if a colored marble is clicked draws an empty marble to replace it
        # since the player cant have duplicate colors
        for colored_marbles in self.colored_marbles:
            if colored_marbles.clicked_in_region(x, y) and not \
                colored_marbles.is_empty:
                color = colored_marbles.get_color()
                # draws an empty marble if clicked
                colored_marbles.draw_empty()
                
        # did not click on a color just return
        if color == None:
            return
        
        # sets the color of the colored marble that is clicked and draws the
        # colored marble in the first open big marble spot
        for big_marbles in self.big_marbles[self.current_row]:
            if big_marbles.is_empty:
                # set color to the colored marble
                big_marbles.set_color(color)
                # draw a colored marble
                big_marbles.draw()
                # color one then stop
                break
    
    def write_player_scores(self):
        """writes the player scores from previous attempts from lowest score
        to highest because the lowest score is the best, writes the scores
        from the scores stored inside the leaderboard file."""
        current_x = 250
        current_y = 340
        # if the leaderboard file doesnt exit insert the error gif and do 
        # nothing since there is nothing to write
        if not os.path.exists("Leaderboard.txt"):
            self.add_gifs('leaderboard_error.gif', 335, 200)
            return
            
        try:
            # read the leaderboard file
            with open('Leaderboard.txt', "r") as leaderboard_info:
                # takes the lines in the leaderboard file and writes however
                # many lines are present inside the file, max: 7
                for lines in leaderboard_info:
                    if not lines.isspace():
                        current_y = current_y - 50
                        self.pen.penup()
                        # sets pen color to black
                        self.pen.color("black")
                        self.pen.goto(current_x, current_y)
                        # writes the lines present in the file
                        self.pen.write(lines, font=("Calibri", 20, "bold"))
                        # leaves the leaderboard scores placed down on the 
                        # window
                        self.pen.stamp()
                        self.pen.pendown()
        # if no leaderboard file, present an error                
        except FileNotFoundError as error:
            # pop us error message gif
            with open('mastermind_errors.err', "a") as errorfile:
                errorfile.write(str(datetime.now()))
                errorfile.write(str((error)))
                errorfile.write("\n")
            return False
        return True
            
    def run_mastermind_game(self):
        """calls all the functions needed to run the game.
        """
        # gets the username/name of the player in order to store in a 
        # leaderboard file
        self.get_user()
        # make the mastermind gameboard, the square that gets the marbles 
        # drawn inside 
        self.draw_gameboard(650, 680)
        # make the leaderboard square that stores highscores
        self.draw_leaderboard(230, 680)
        # make the game objects square with the colored marbles to guess with, 
        # the check/x button and the quit button
        self.hold_game_clickables(930, 140)
        # insert the gifs including any picture that is present on the board, 
        # the check/ x button and the quit button
        self.gifs()
        # making the marbles for when the player has the guess the code
        self.draw_empty_marbles()
        # making the colored marbles that the player starts with in order 
        # to guess the correct code the ai wants
        self.draw_colored_marbles()
        # make a file in order to store high scores for furture players to see
        self.draw_high_score_header()
        # make a random code for the player to guess
        self.make_a_random_color_code()
        # makes a leaderboard
        self.write_player_scores()
        # keeps the game running until the players clicks the quit button
        turtle.mainloop()
