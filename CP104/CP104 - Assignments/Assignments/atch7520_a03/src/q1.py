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
balloons = int(input("Enter number of balloons:"))
kids = int(input("Enter number of children:"))

# Number of balloons per kids
x = balloons // kids

# Leftover/Remainder
y = balloons - (kids * x)

print("Each child will receive {:.0f} balloons".format(x))

print("Balloons that wont be distributed: {:.0f}".format(y))

