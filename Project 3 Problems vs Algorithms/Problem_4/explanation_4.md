# Data Structures and Algorithms Nanodegree  
## Project 3- Problems vs Algorithms
### Problem 4- Dutch National Flag Problem
  
   
- The problem statement asks to sort the array in asigle traversal. Hence, divide and conquer approach is used.
- There are three index pointers used- two starting from 0 and one starting from last element in array.
- One index pointer starting from 0 is used to traverse the array.
- If an element has value of 2, it is put at the end of the array; if it is 0, it is kept at front; else traversing index is updated by 1  
  
Time Complexity-  
- O(n)  
  
Space complexity-  
- O(# of elements in the array)