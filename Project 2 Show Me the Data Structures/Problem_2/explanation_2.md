# Data Structures and Algorithms Nanodegree
## Project 2- Show Me the Data Structures
### Problem 2- File Recursion

In this problem, all the files with a given suffix are returned on giving suffix and working directory as input. Recursive approach is used for this problem.
- A function find_files is called recursively that lists files and folders in a directory.
- All the files found in given directory are checked if they end with given suffix.
- If the folder ends with given suffix, it is appended to the output_list.
- If a folder is encountered, then find_files() is called on that folder.

Time Complexity-
- O(# terminal nodes in working directory)  
  
Space Complexity-
- O(# files with given suffix)