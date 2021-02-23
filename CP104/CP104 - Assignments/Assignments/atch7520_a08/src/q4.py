"""
------------------------------------------------------------------------
question 4
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-11-16"
------------------------------------------------------------------------
"""
from a8_functions import is_word_chain


def main():
    user_in = input("Enter a list of strings: ").split(", ")
    result = is_word_chain(user_in) 
    print() 
    if(result):
        print("That list is a word chain!")     
    else:
        print("That list is not a word chain!")

    
main()
