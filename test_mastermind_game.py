from game_board import MastermindBoard
from mastermind_game import main
import unittest 
import shutil
import os

class MastermindTest(unittest.TestCase):
    
    def test_make_a_random_color_code(self):
        """testing the secret code generation makine sure there are no 
        duplicates.
        """
        for _ in range(4):
            code = MastermindBoard()
            code.draw_colored_marbles()
            color_code = code.make_a_random_color_code()
            colors_in_color_code = []
            # generate a random code and make sure there arent any duplicates
            # assertTrue if the colors arent in the random color code to create
            # a list of four random colors
            for marble in color_code:
                self.assertTrue(marble.get_color() not in colors_in_color_code)
                colors_in_color_code.append(marble.get_color())
        
    def test_check_if_color_in_secret_code(self):
        """testing to see if the color is in the secret code but not in the 
        correct spot. will return true if it is and false if its not.
        """
        for _ in range(4):
            code = MastermindBoard()
            code.draw_colored_marbles()
            color_code = code.make_a_random_color_code()
            colors_in_color_code = []
            # put the marbles in a list
            for marble in color_code:
                colors_in_color_code.append(marble.get_color())
            # if the marble color matches a color inside the code assertTrue
            # otherwiser assertFalse
            for marble in color_code:
                if marble.get_color() in colors_in_color_code:
                    self.assertTrue(code.check_if_color_in_color_code(marble))
                else:
                    self.assertFalse(code.check_if_color_in_color_code(marble))
                
    def test_error_logging(self):
        """testing functions that need certain files to exist. what happens
        when the functions dont have those files 
        """
        test = MastermindBoard()
        # https://www.geeksforgeeks.org/python-shutil-move-method/
        # use shutil in order to move file to test for file not found errors
        shutil.move("checkbutton.gif", "checkbutton.gif.temp")
        try:
            self.assertRaises(FileNotFoundError, test.run_mastermind_game)
        except Exception:
            shutil.move("checkbutton.gif.temp", "checkbutton.gif")
            raise Exception()
        shutil.move("checkbutton.gif.temp", "checkbutton.gif")
        
        # if leaderboard test exists move the file and test for exceptions
        if os.path.exists("Leaderboard.txt"):
            shutil.move("Leaderboard.txt", "Leaderboard.txt.temp")
        try:
            self.assertTrue(test.write_player_scores)
        except Exception:
            if os.path.exists("Leaderboard.txt.temp"):
                shutil.move("Leaderboard.txt.temp", "Leaderboard.txt")
            raise Exception()
        if os.path.exists("Leaderboard.txt.temp"):
            shutil.move("Leaderboard.txt.temp", "Leaderboard.txt")
        
if __name__ == "__main__":
    unittest.main()
