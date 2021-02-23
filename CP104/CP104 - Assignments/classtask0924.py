"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-09-24"


Jordan Kang
180196720 

Martin Gomes
190198390

Sanskar Srivastava
193332930

Kerri Vandermeer
176701930

------------------------------------------------------------------------
"""
import math

# asks user for two numbers to perform operations with
n1, n2 = input("Enter two numbers you'd like to do operations on: ").split()

# Variables for passing into calculator functions being type casted as floats for proper use
n1 = float(n1)
n2 = float(n2)


def addition(x, y):
    x = float(x)
    y = float(y)
    a = x + y
    return a


def subtraction(x, y):
    x = float(x)
    y = float(y)
    a = x - y
    return a


def multiplication(x, y):
    x = float(x)
    y = float(y)
    a = x * y
    return a 


def division(x, y):
    x = float(x)
    y = float(y)
    a = x / y
    return a 


def powers(x, y):
    a = x ** y
    return a 


def kineticEnergy(x, y):  # assume x is mass and y is velocity
    ke = (0.5 * x * (math.pow(y, 2)))
    return ke

    
def potentialEnergy(x, y):  # assume x is mass and y is height
    g = 9.8
    pe = (x * y * g)
    return pe
    
    
