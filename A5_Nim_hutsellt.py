##############################################################################
# Author: Tyler Hutsell
# Username: hutsellt
#
# Assignment: A5
# Purpose: Gain practice using fruitful functions, iteration, and modulus when
# writing code. Also gain practice using top-down coding design.
##############################################################################
import random


def get_balls():
    """
    This function will request user input for the number of balls they want to
     play Nim with. It will also ensure that this number is at least 15.
    :return: tot_balls
    """
    tot_balls = int(input("Select a number of balls for playing Nim.(15+)"))
    while tot_balls < 15:
        print("You must select 15 balls or more")
        get_balls()
    return tot_balls


def user_pick():
    """
    This is the function that will be referred to for the user player's turn.
    It will ask for input of their choice of number of balls to remove.
    :return: play_take
    """
    play_take = int(input("How many balls would you like to remove?(1-4)"))
    while 1 <= play_take <= 4:
        return play_take
    else:
        print("You may only take between 1 and 4 balls")
        user_pick()


def com_pick(balls):
    """
    This si the function that will handle the computer's turn. It will
    hopefully be optimized so that the computer will win whenever possible.
    :param balls: This input is necessary for the current total of balls in
    play.
    :return: com_take
    """
    # Because the computer decision making is based on code alone, it will be
    # more complex than the user's.
    a = (balls - 1)
    b = (balls - 2)
    c = (balls - 3)
    d = (balls - 4)
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
        com_take = random.randint(1, 4)
    return com_take


def play_nim(balls):
    """
    This function will provide the general code for the game Nim,
    calling the functions that handle players' turns. The function will monitor
    that total number of balls during game play, and declare a winner when
    a player has taken the last ball.
    :param balls: The total balls the game begins with is needed for playing
    the game.
    :return: None
    """
    while balls > 0:
        balls = balls - user_pick()
        if balls <= 0:
            print("Congratulations! You win!")
            break
        print("The total of balls remaining is " + str(balls))
        print("Time for the computer's turn!")
        balls = balls - com_pick(balls)
        if balls <= 0:
            print("Sorry! The computer wins!")
        print("The total of balls remaining is " + str(balls))
    else:
        print("Thank you for playing the game of Nim!")


def main():
    """
    Our main function will call all necessary functions to play the game of
    Nim; with the computer programed to be the most likely to win.
    :return: None
    """
    balls = get_balls()
    play_nim(balls)


main()
