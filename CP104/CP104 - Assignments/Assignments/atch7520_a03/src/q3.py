"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-09-26"
------------------------------------------------------------------------
"""
number = int(input("Enter a positive two digit integer:"))

x = number // 10

y = number - (x * 10)

summation = x + y

print("The sum of the two digits in the integer ({}) is: {}".format(number, summation))

