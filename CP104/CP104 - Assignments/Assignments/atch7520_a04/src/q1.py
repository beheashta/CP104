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
from q1_functions import calc_federal_tax
from q1_functions import calc_prov_tax

inc = float(input("Enter your income:"))

fed = calc_federal_tax(inc)
prov = calc_prov_tax(inc)
tot_tax = fed + prov

text = '''
Your total tax liability is: $ {:.0f} 
[details federal tax: $ {:.0f}, state tax: $ {:.0f}]
''' .format(tot_tax, fed, prov)

print(text)
