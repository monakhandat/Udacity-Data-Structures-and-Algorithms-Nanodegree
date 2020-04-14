#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0: # For negative numbers return -1
        return -1
    
    if number == 0 or number == 1 : 
        return number 
   
    start_number = 1
    end_number = number    
    while (start_number <= end_number) : 
        middle_number = (start_number + end_number) // 2
          
        
        if middle_number*middle_number == number : 
            return middle_number 
              
        
        if middle_number * middle_number < number : 
            start_number = middle_number + 1
            squareroot = middle_number 
              
        else : 
            end_number = middle_number-1
              
    return squareroot 

print ("Pass" if  (3 == sqrt(9)) else "Fail") # Expected output- Pass as sqrt(9) = 3
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Expected output- Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Expected output- Pass as sqrt(16) = 4
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Expected output- Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Expected output- Pass as nearest integer to sqrt(27) = 5

print("Pass" if  (-1 == sqrt(-2300)) else "Fail") # Expected output- Pass
# Test case to print square root of 100**100
print("Pass" if (10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 == sqrt(100**100)) else "Fail")

