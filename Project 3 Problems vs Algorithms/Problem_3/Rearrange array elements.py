#!/usr/bin/env python
# coding: utf-8

# In[9]:


def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = mergesort(input_list)
    length = len(sorted_list)
    first_number = 0
    second_number = 0
    for i in range(0,length,2):
        first_number = first_number*10 + sorted_list[i]
        if i < length-1:
            second_number = second_number*10 + sorted_list[i+1]
    
    return first_number,second_number


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test Case 1
test_function([[1, 2, 3, 4, 5], [542, 31]]) # Expected output- Pass

# Test Case 2- with repeated digits
test_function([[9, 8, 7, 1, 2, 3, 4, 5, 5], [97531, 8542]]) # Expected output- Pass

# Test Case 3- with no number
test_function([[],[]]) # Expected output- Pass

# Test Case 4- with only one number
test_function([[1],[1,0]]) # Expected output- Pass

