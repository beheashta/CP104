"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-09-27"
------------------------------------------------------------------------
"""

'''
-------------------------------------------------------
Calculates the average for three quiz scores
Use: avg = average_score(quiz1score, quiz2score, quiz3score)
-------------------------------------------------------
Parameters:
    grams_fat - fat grams conusmed (float >= 0)
    grams_carbs - carbohydrate grams consumed (float >= 0)
Returns:
    fatCals - the amount of fat calories consumed (float >= 0)
    carbsCals - the amount of carbohydrate calories consumed (float >= 0)
    totalCals - the total combined amount of fat and carbohydrate calories consumed (float >= 0)
-------------------------------------------------------
'''


def calorie_calculator(grams_fat, grams_carb):
    fatCals = (grams_fat * 9)
    carbsCals = (grams_carb * 4)
    totalCals = (fatCals + carbsCals)
    return(fatCals, carbsCals, totalCals)

# ----------------- Main Code ------------------------------------------------------------


# User entry for fat grams and carbohydrate grams consumed
gramsF = float(input("Enter the fat grams consumed:"))
gramsC = float(input("Enter the carbohydrate grams consumed:"))

# using the calorie_calculator function to create three variables which store the current value of each measurement
fat, carbs, total = calorie_calculator(gramsF, gramsC)

# final formatted print statement using the values straight from the function 
print("Total calories a total of {:.0f} [Fat calories {:.2f} and Carbohydrate calories {:.2f}]".format(total, fat, carbs))
