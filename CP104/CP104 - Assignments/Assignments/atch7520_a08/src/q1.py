"""
------------------------------------------------------------------------
question 1
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-11-16"
------------------------------------------------------------------------
"""

from a8_functions import sum_digit_string


def main():
    userIn = input("Enter a string of numbers to be summed up by single digits: ")
    result = sum_digit_string(userIn)
    print("")
    print("The sum of the digits in this string is {}".format(result)) 

     
main()
