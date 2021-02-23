"""
------------------------------------------------------------------------
question 2
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-11-16"
------------------------------------------------------------------------
"""

from a8_functions import find_frequent


def main():
    userIn = input("Enter a string: ")
    result = find_frequent(userIn)    
    print()
    print("The most frequently occurring characters in this string are: {}".format(result)) 
    
    
main()
