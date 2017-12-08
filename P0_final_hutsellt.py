##############################################################################
# Author: Tyler Hutsell
# Username: hutsellt
#
# Assignment: P0
# Purpose:
##############################################################################
# Acknowledgements:
#
##############################################################################

import random
from math import sqrt
import turtle
global num_dots


class NimBoard:
    """
    This class manages the visual game board for playing Nim
    """
    def __init__(self):
        # self.piles = 0
        self.objects = 0

    def calculate_size(self, num_dots):
        """
        This function takes the user input (num_dots) and calculates the best
        display to make a square shape (equal number of dots across and down)
        :param num_dots: The chosen number of dots to display
        :return: Number of dots across, number of dots down (width, height)
        """
        self.objects = num_dots
        square = sqrt(self.objects)
        if self.objects % square == 0:
            return int(square), int(square)
        else:
            denom = self.objects // sqrt(self.objects)
            while self.objects % denom != 0:
                denom -= 1
            return int(denom), int(self.objects // denom)

    def is_valid_size(self, dot_width, dot_height, distance, screen_width, screen_height):
        """
        This function tests if the chosen number of dots, a chosen number of
        pixels apart, will fit on the maximum screen size as set values.
        :param dot_width: Calculate number of dots across (width)
        :param dot_height: Calculated number of dots down (height)
        :param distance: The maximum distance across that the dots are displayed
        :param screen_width: The set width of the Turtle Screen
        :param screen_height: The set height of the Turtle Screen
        :return: True if the dots will fit on the screen or False if dots will not
        """
        if dot_width * distance > screen_width or dot_height * distance > screen_height:
            return False
        return True

    def draw_board(self, dot_distance, dottie, height, width):
        """
        This function draws the "game board" the square shape formed by the dots
        :param dot_distance: The screen width (maximum width of "square")
        :param dottie: Our turtle object
        :param height: Calculated height of dot "square"
        :param width: Calculated width of dot "square"
        :return: None
        """
        for y in range(height):
            for i in range(width):
                dottie.dot()
                dottie.forward(dot_distance)
            dottie.backward(dot_distance * width)
            dottie.right(90)
            dottie.forward(dot_distance)
            dottie.left(90)

    def user_input(self, screen_height, screen_width):
        """
        This function takes user input, asking for how many dots they would like,
        it then feeds this number into the calculate_size() function to fit
        the dots into a square or rectangular shape of even filled rows.
        It then asks the user how many pixels apart they would like the dots,
        and runs that number in the is_valid_size function().
        :param screen_height: The set height of the turtle window
        :param screen_width: The set width of the turtle window
        :return: Values for dot_distance (The spacing between dots),
        height (The number of dots up and down),
        and width (The number of dots across)
        """
        global num_dots
        num_dots = "x"
        print("Welcome to the game of Nim!")
        while not num_dots.isnumeric():
            num_dots = input("How many dots do you want to play with? ")
        num_dots = int(num_dots)
        (width, height) = self.calculate_size(num_dots)
        dot_distance = screen_width
        first = False
        while not self.is_valid_size(width, height, dot_distance, screen_width, screen_height):
            if first:
                print("That won't fit on the screen; pick a smaller number")
            dot_distance = input("How far apart are the dots? ")
            while not dot_distance.isnumeric():
                dot_distance = input("Let's try an integer instead. \nHow far apart are the dots? ")
            first = True
            dot_distance = int(dot_distance)
        return dot_distance, height, width


class ComAI:
    """
    This class will manage the computer AI's move set during Nim game play
    """
    def __init__(self):
        self.gamemode = "normal"

    def com_pick_normal(self):
        """
        This is the function that will handle the computer's turn. It will
        hopefully be optimized so that the computer will win whenever possible.
        :param balls: This input is necessary for the current total of balls in
        play.
        :return: com_take
        """
        # Because the computer decision making is based on code alone, it will be
        # more complex than the user's.
        a = (num_dots - 1)
        b = (num_dots - 2)
        c = (num_dots - 3)
        d = (num_dots - 4)
        # It is the computers best strategy to leave a number of balls divisible
        # by 5 when possible. This code checks for that possibility and chooses
        # thus, otherwise picks randomly as it will not matter until the user
        # makes a mistake. Credit: Scott Heggen's tip in A5
        if a % 5 == 0:
            com_take = 1
        elif b % 5 == 0:
            com_take = 2
        elif c % 5 == 0:
            com_take = 3
        elif d % 5 == 0:
            com_take = 4
        else:
            com_take = random.randint(1, num_dots-4)
        return com_take


class GamePlay:
    """
    This class manages the active game play elements of Nim
    """
    def __init__(self):
        self.gamemode = "normal"

    # def game_select(self):
    #    """
    #    This function prompts the user to indicate which version (rule set) of
    #    Nim they wish to play
    #    :return: self.gamemode; the selected game mode to play
    #    """
    #    while True:
    #        self.gamemode = input("Which game mode would you like to play(normal)(misery)?")
    #        if self.gamemode is "normal" or "misery":
    #            self.new_game = Nim_board(self.gamemode)
    #        else:
    #            print("You must select a valid game mode:(normal)(misery)")
    #    return self.gamemode

    def play_nim(self):
        """
        This function will provide the general code for the game Nim,
        calling the functions that handle players' turns. The function will monitor
        that total number of balls during game play, and declare a winner when
        a player has taken the last ball.
        :return: None
        """
        wn = turtle.Screen()
        screen_width = 1100
        screen_height = 650
        wn.setup(width=screen_width, height=screen_height, startx=0, starty=0)

        dottie = turtle.Turtle()
        dottie.penup()
        dottie.setpos(-(screen_width/2-50), screen_height/2-25)

        board = NimBoard()
        (dot_distance, height, width) = board.user_input(screen_height, screen_width)
        board.draw_board(dot_distance, dottie, height, width)
        dottie.hideturtle()

        # while num_dots > 0:
        #    num_dots = num_dots - user_pick()
        #    if num_dots <= 0:
        #        print("Congratulations! You win!")
        #        break
        #    print("The total of dots remaining is " + str(num_dots))
        #    print("Time for the computer's turn!")
        #    num_dots = num_dots - ComAI.com_pick_normal(num_dots)
        #    if num_dots <= 0:
        #        print("Sorry! The computer wins!")
        #    print("The total of dots remaining is " + str(num_dots))
        # else:
        #    print("Thank you for playing the game of Nim!")


def main():
    new_game = GamePlay()
    new_game.play_nim()

if __name__ == "__main__":
    main()

