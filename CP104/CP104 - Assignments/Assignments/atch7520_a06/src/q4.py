"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-10-26"
------------------------------------------------------------------------
"""

from a6_functions import its_prime

t = int(input("Enter a positive integer:"))

if t < 0:
    t = int(input("Enter a positive integer:"))
    
k = its_prime(t)

if k == True:
    print("{} is a prime number".format(t))

else:
    print("{} is not a prime number".format(t))
    
    
