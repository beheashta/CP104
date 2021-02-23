
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


def calc_profit(principal, year):
    """
    -------------------------------------------------------

    Calculates the value of the investment every year

    Use: profit = calc_profit(principal,year)

    -------------------------------------------------------

    Parameters:

        principal - the amount of money to invest in the house (float > 0)

        year - the number of years of investment (int > 0)

    Returns:
    
    -------------------------------------------------------
    """
    print("")
    print("Year  Value (Million Dollars)")
    print("----  -----------------------")
    for x in range(1, year + 1):        
        principal = (principal * 1.05)
        print("{:>4} {:>24.6f}".format(x, principal / 1000000))


def perfect_square(num):
    """
    -------------------------------------------------------
    while loop is better due to ease of code writing.
    
    finds all perfect squares below a given number

    Use: square = perfect_square(num)

    -------------------------------------------------------

    Parameters:

        num - the final number to square
    
    -------------------------------------------------------
    """
    x = 1
    if num > 1:
        k = ("Perfect Squares below {} are: 1".format(num))
        while x < num:
            if ((x ** (1 / 2) % 1)) == 0 and x > 1:
                k += "," + (str(x))
            x += 1
        print(k)
    else:
        print("You did not enter a positive integer.")
        
        
def factorial(num):
    """
    -------------------------------------------------------
    Use: results = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number input by user
        
    Returns:
        ans - answer
    -------------------------------------------------------
        """
        
    if num >= 0:
        total = (1)
        for i in range(1, num + 1, 1):
            total *= i
        print("{}! = {}".format(num, total), end="")
            
    else:
        print("You did not enter a positive integer.")


def its_prime(num):
    '''
    -------------------------------------------------------
    Use: results = its_prime(num)
    -------------------------------------------------------

    Parameters:

        num - number input by user
        
    Returns:
        prime - true or false
    -------------------------------------------------------
    '''
    prime = True
    i = 2
    
    while(prime and i < num):
        if num % i == 0:
            prime = False
            
        i += 1
    return prime
        
        
