"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-10-05"
------------------------------------------------------------------------
"""


def calc_federal_tax(income):
    """
    -------------------------------------------------------

    Calculates federal tax

    Use: federal = calc_federal_tax(income)

    -------------------------------------------------------

    Parameters:

        income - income amount (int > 0)
        
    Returns

        tax - federal tax amount depending on income (float >= 0)

    -------------------------------------------------------
    """
    if income <= 35000:
        tax = income * 0.15
        return(tax)
    
    if income >= 35001 or income <= 100000:
        tax = income * 0.25
        return(tax)
    
    if income > 100000:
        
        p = income - 35000
        
        t1 = (35000 * 0.15)  # the first 35000
        
        if p == 100000:
            tax = (t1 + (100000 * 0.25))
            return(tax)

        if p > 100000:
            
            b = p % 100000
            taxB = b * 0.25
            
            c = p - b
            taxC = c * 0.35
            
            tax = (t1 + taxB + taxC)
            return(tax)


def calc_prov_tax(income):
    """
    -------------------------------------------------------

    Calculates provincial tax

    Use: federal = calc_federal_tax(income)

    -------------------------------------------------------

    Parameters:

        income - income amount (int > 0)
        
    Returns

        tax - provincial tax amount depending on income (float >= 0)

    -------------------------------------------------------
    """
    if income <= 50000:
        tax = 0 
        return(tax)
    
    else:
        tax = income * 0.05
        return(tax)
