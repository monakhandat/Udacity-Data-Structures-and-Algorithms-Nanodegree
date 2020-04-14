from collections import OrderedDict

class LRU_Cache(OrderedDict):
    """
    LRU_cache uses OrderedDict to arrange the items in cache with most used items on top
    and least used at the bottom; when a new item is added, the least used item from bottom
    is deleted
    """

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        

    def get_item(self, key):
        """
        Retrieve item from provided key. 
        Return -1 if not in cache 
        """
        if not self.get(key):
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. 
        If the cache is at capacity remove the oldest item.
        """ 
        self[key]= value
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last = False)


def test_function(cache,key, solution):
    """
    test function takes cache, key and expected output as input and gives the test result as pass or fail
    bu comparing LRU output with expected output
    """
    if cache.get_item(key) == solution:
        print("Passed test with key: ", key)
    else:
        print("Fail")
    
    return 

# Test Case 1
print("Test Case 1")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.get_item(1)       # returns 1
our_cache.get_item(2)       # returns 2
our_cache.get_item(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get_item(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
test_function(our_cache,6, 6)
test_function(our_cache,9, -1)
test_function(our_cache,3, -1)
print("-"*100)

# Test Case 2- Empty cache
print("Test Case 2")
our_cache = LRU_Cache(0)
our_cache.set(1, 1)

our_cache.get_item(1)       # returns 1

our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get_item(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
test_function(our_cache,1, -1) # Expected output-  Passed test with key:  1
test_function(our_cache,5, -1) # Expected output-  Passed test with key: 5
test_function(our_cache,6, -1) # Expected output-  Passed test with key: 6
print("-"*100)


# Test Case 3
print("Test Case 3")
our_cache = LRU_Cache(10)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.get_item(1)       # returns 1
our_cache.get_item(2)       # returns 2
our_cache.get_item(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get_item(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
test_function(our_cache,6, 6) # Expected output-  Passed test with key:  6
test_function(our_cache,10, -1) # Expected output-  Passed test with key:  10; 10 not present in cache
test_function(our_cache,3, 3) # Expected output-  Passed test with key:  3
print("-"*100)







