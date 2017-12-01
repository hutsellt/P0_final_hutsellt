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

import sys
from t12_dots_hutsellt_grantr import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def dots_test_suite():
    """
    The dots_test_suite() is designed to test the following:
      calculate_size()
      is_valid_size()
      user_input()

    :return: None
    """

    # The following tests the calculate_size() function
    print("\nTesting calculate_size()")
    testit(calculate_size(25) == (5, 5))
    testit(calculate_size(5) == (1, 5))
    testit(calculate_size(50) == (5, 10))
    testit(calculate_size(30) == (5, 6))
    testit(calculate_size(10) == (2, 5))

    # The following tests the is_valid_size() function
    print("\nTesting is_valid_size()")
    testit(is_valid_size(5, 5, 1100, 1100, 650) == False)
    testit(is_valid_size(5, 5, 5, 1100, 650) == True)
    testit(is_valid_size(1, 5, 5, 1100, 650) == True)
    testit(is_valid_size(5, 10, 2, 1100, 650) == True)
    testit(is_valid_size(5, 6, 10, 1100, 650) == True)
    testit(is_valid_size(2, 5, 20, 1100, 650) == True)
    testit(is_valid_size(5, 5, 200, 1100, 650) == False)

    # The following tests the user_input() function
    # This test actually tests the above functions as well, as user_input
    # calls these functions.
    print("\nTesting user_input()")
    testit(user_input(1100, 650) == (5, 5, 5))  # For 25 dots, 5 pixels apart
    testit(user_input(1100, 650) == (2, 5, 1))  # For 5 dots, 2 pixels apart
    testit(user_input(1100, 650) == (10, 10, 5))  # For 50 dots, 10 pixels apart

dots_test_suite()
