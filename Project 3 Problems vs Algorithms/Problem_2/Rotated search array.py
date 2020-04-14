
def divide_array(input_list, start, end,result = -1):
    """
    Returns the index from where current input list is rotated
    """
    
    mid = (start+end)//2
    #if input_list[start] < input_list[middle] and input_list[middle] < input_list[end]: # sorted array
    #    return result
    if start == mid:
        return start
    if input_list[start] > input_list[mid] and input_list[mid] < input_list[end]:
        result = divide_array(input_list, start, mid, result)
    elif input_list[start] < input_list[mid] and input_list[mid] > input_list[end]:
        result = divide_array(input_list, mid, end, result)
    return result
    
def binary_search(divided_array,number,start,end,result=-1):
    """
    Performs binary search on two sorted arrays to find given number,
    returns index of the number from one of the sorted arrays
    If number is not present, -1 is returned
    """
    #if start == end:
        
    if number == divided_array[start]:
        return start
    if number == divided_array[end]:
        return end
    mid = (start + end) // 2
    if mid >= len(divided_array):
        return result
    
    if number == divided_array[mid]:
        return mid
    if mid<end and number > divided_array[mid]:
        result = binary_search(divided_array,number,mid+1,end,result)
    if start < end and number < divided_array[mid]:
        result = binary_search(divided_array,number,start,mid-1,result)
    
    return result

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1
    partition_index = divide_array(input_list, 0, len(input_list)-1)
    divided_array_1 = input_list[:partition_index+1]
    divided_array_2 = input_list[partition_index+1:]
    
    if divided_array_1:
        num_at_index = binary_search(divided_array_1,number,0,len(divided_array_1)-1)
        if num_at_index != -1:
            return num_at_index
        else:
            num_at_index = binary_search(divided_array_2,number,0,len(divided_array_2)-1)
            return partition_index+num_at_index+1 if num_at_index != -1 else -1
    
    elif divided_array_2:
        num_at_index = binary_search(divided_array_2,number,0,len(divided_array_2)-1)
        return num_at_index
    
    else:
        return -1
        

    
def linear_search(input_list, number):
    """
    Used to compare with the result from rotated_array_search
    """
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    """
    compare results from linear_search and rotated_array_search
    """
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print("-"*100)
# Added an array by rotating circularly and checking if rotated_array_search works for each
# of the rotated position of array

# Searching for the last element in array
test_function([[7,1,2,3,4,5,6], 6]) # Expected output- Pass
print("-"*100)
test_function([[6,7,1,2,3,4,5], 1]) # Expected output- Pass
print("-"*100)

# Searching for non-existing number in array
test_function([[5,6,7,1,2,3,4], 8]) # Expected output- Pass
print("-"*100)

# Searching for the first element in array
test_function([[4,5,6,7,1,2,3], 4]) # Expected output- Pass
print("-"*100)

# Searching for the middle element in array
test_function([[3,4,5,6,7,1,2], 6]) # Expected output- Pass
print("-"*100)
test_function([[2,3,4,5,6,7,1], 10]) # Expected output- Pass
print("-"*100)
test_function([[1,2,3,4,5,6,7], 10]) # Expected output- Pass
print("-"*100)
# Test case to check for empty array
test_function([[], 10]) # Expected output- Pass