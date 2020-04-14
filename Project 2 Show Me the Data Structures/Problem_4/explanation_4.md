# Data Structures and Algorithms Nanodegree
## Project 2- Show Me the Data Structures
### Problem 4- Active Directory



- In this problem, recursion is used to find and list users in all the groups including subgroups.  
- Recursion searches nested groups and a nested list is created of all the users in given group including subgroup.  
- flat_list method creates a flat list of all the users.  
- If the user is present in the list, True is returned. 
  
Time Complexity-
- O(# of groups in the given directory)
  
Space Complexity-
- O(# of users in the directory)