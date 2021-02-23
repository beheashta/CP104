"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2019-11-16"
------------------------------------------------------------------------
"""


def sum_digit_string(my_str): 
    """ 
    -------------------------------------------------------
    Sums all the digits in my_str, ignores non-digit characters
    Use: total = sum_digit_string (my_str) 
    -------------------------------------------------------
    Parameters: 
        my_str: string that has single-digit numbers (str)
    Returns 
        total: sum of all the single digit number (integer >= 0) 
    -------------------------------------------------------
    """
    if len(my_str) > 0 :
        total = 0
        for x in my_str:
            if(x.isdigit()):
                total += int(x)
                
            else:
                continue
        
    else:
        total = None
        
    return total


def find_frequent(my_str):
    """ 
    -------------------------------------------------------
    Finds all the non-whitespace characters within a string
    that have the highest occurrence. 
    
    Use: characters = find_frequent(my_str) 
    -------------------------------------------------------
    Parameters: 
        my_str: string that has to be checked
        
    Returns 
        result: A list of characters that have the highest occurrence (list[integer], len() >= 0) 
    -------------------------------------------------------
    """    
    
    if(len(my_str) > 0):
        most_frequent = -1
        for x in my_str:
            count = my_str.count(x)
            if(x.isspace() == False and count > most_frequent):
                most_frequent = count
    
            else:
                continue
    
        result = []
        for x in my_str:
            if(x.isspace() == False and x not in result and my_str.count(x) == most_frequent):
                result.append(x)
                
            else:
                continue
    
    else:
        result = None
        
    return result


def string_capitalizer(my_str):
    """ 
    -------------------------------------------------------
    Converts a string to proper sentence case, capitalizing letters
    after a '?' or '.'
    
    Use: result = string_capitalizer(my_str) 
    -------------------------------------------------------
    Parameters: 
        my_str: The sentence to be converted.
        
    Returns 
        result: The resultant sentence (string) 
    -------------------------------------------------------
    """  
    length = len(my_str)
    if(length > 0):
        result = my_str[0].capitalize() + my_str[1]
        for i in range(2, length):
            if(my_str[i - 2] == '?' or my_str[i - 2] == '.'):
                result += my_str[i].capitalize()
                
            else:
                result += my_str[i]
        
    else:
        result = None
    
    return result
    

def is_word_chain(my_list):
    """ 
    -------------------------------------------------------
    Checks to see whether or not a list of strings forms a 
    word chain.
    
    Use: result = is_word_chain(my_list) 
    -------------------------------------------------------
    Parameters: 
        my_list: A list of strings to be checked
        
    Returns 
        result: Whether or not the list is a word chain (boolean) 
    -------------------------------------------------------
    """  
    result = True
    i = 0
    
    while(i < len(my_list) - 1 and result):
        if(my_list[i][-1].lower() != my_list[i + 1][0].lower()):
            result = False
            
        i += 1
    
    return result

