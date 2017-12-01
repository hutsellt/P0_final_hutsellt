######################################################################
# Author: Tyler Hutsell & Rodney Grant     Done: Change this to your names
# Username: hutsellt & grantr             Done: Change this to your usernames
#
# Assignment: T12: Modules
#
# Purpose: A special game from my (and likely, many of your) childhood
#
######################################################################
# Acknowledgements:
#
# Idea inspired by original code from: https://michael0x2a.com/blog/turtle-examples
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle               # Notice the different ways we can import modules
from math import sqrt       # Notice the different ways we can import modules; there's one more way...


def calculate_size(num_dots):
    """
    This function takes the user input (num_dots) and calculates the best
    display to make a square shape (equal number of dots across and down)
    :param num_dots: User input of number of dots
    :return: Number of dots across, number of dots down (width, height)
    """
    square = sqrt(num_dots)
    if num_dots % square == 0:
        return int(square), int(square)
    else:
        denom = num_dots // sqrt(num_dots)
        while num_dots % denom != 0:
            denom -= 1
        return int(denom), int(num_dots // denom)


def is_valid_size(dot_width, dot_height, distance, screen_width, screen_height):
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


def draw_board(dot_distance, dottie, height, width):
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


def user_input(screen_height, screen_width):
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
    num_dots = "x"
    while not num_dots.isnumeric():
        num_dots = input("How many dots do you want? ")
    num_dots = int(num_dots)
    (width, height) = calculate_size(num_dots)
    dot_distance = screen_width
    first = False
    while not is_valid_size(width, height, dot_distance, screen_width, screen_height):
        if first:
            print("That won't fit on the screen; pick a smaller number")
        dot_distance = input("How far apart are the dots? ")
        while not dot_distance.isnumeric():
            dot_distance = input("Let's try an integer instead. \nHow far apart are the dots? ")
        first = True
        dot_distance = int(dot_distance)
    return dot_distance, height, width


def main():
    wn = turtle.Screen()
    screen_width = 1100
    screen_height = 650
    wn.setup(width=screen_width, height=screen_height, startx=0, starty=0)

    dottie = turtle.Turtle()
    dottie.penup()
    dottie.setpos(-(screen_width/2-50), screen_height/2-25)

    (dot_distance, height, width) = user_input(screen_height, screen_width)
    draw_board(dot_distance, dottie, height, width)
    dottie.hideturtle()

    wn.exitonclick()


if __name__ == "__main__":
    main()
