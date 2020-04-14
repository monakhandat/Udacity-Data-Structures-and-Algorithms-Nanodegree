#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None
    
    min_number = ints[0]
    max_number = ints[0]
    
    for i in ints:
        if i < min_number:
            min_number = i
        if i > max_number:
            max_number = i
    
    return min_number, max_number

import random
# Test Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") # Expected output- Pass

# Test Case 2- Repeated numbers
l = [12,23,45,67,23,12,98,56,101,200]
random.shuffle(l)
print ("Pass" if ((12, 200) == get_min_max(l)) else "Fail") # Expected output- Pass

# Test Case 3- Empty list
l = []
print ("Pass" if (None == get_min_max(l)) else "Fail") # Expected output- Pass

