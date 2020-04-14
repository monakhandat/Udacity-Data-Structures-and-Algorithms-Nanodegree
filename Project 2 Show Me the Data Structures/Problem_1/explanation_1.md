# Data Structures and Algorithms Nanodegree
## Project 2- Show Me the Data Structures
### Problem 1- Least Recently Used Cache 

Least Recently Used Cache makes use of OrderedDict data structure to keep most recently used key, value pairs on top and least recently used at the bottom of the dictionary. LRU works in a LIFO manner, except that whenever an item from cache is called, it needs to be put back on the top.   
  
Time complexity:  
- get_item()- O(1) since I used OrderedDict method get(key) with constant time complexity to search for key value in LRUCache object
- set()- O(1) since both move_to_end and popitem methods in OrderedDict have constant time complexities

Space complexity:   
- O(capacity) since space used by the LRUCache class is dependent upon the capacity defined by the user. In the worst case, only one more element than the capacity is stored in the memory.  
