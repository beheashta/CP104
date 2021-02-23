"""
------------------------------------------------------------------------
question 3
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-11-16"
------------------------------------------------------------------------
"""

from a8_functions import string_capitalizer


def main():
    userIn = input("Enter a string:")
    result = string_capitalizer(userIn)   
    print("")
    print("The proper sentence would be: {}".format(result))
    
    
main()
