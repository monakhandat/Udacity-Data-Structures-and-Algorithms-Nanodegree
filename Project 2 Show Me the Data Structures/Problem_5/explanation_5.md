# Data Structures and Algorithms Nanodegree  
## Project 2- Show Me the Data Structures  
### Problem 5- Blockchain Implementation  
  
  
- First design decision was to use Block class object in Node for LinkedList
- In Blockchain LinkedList, the next node is linked to its previous node
- In terms of the Block object, previous_hash of next block is current Block i.e., current node of the LinkedList
  
Time Complexity:  
- O(n) for append
- O(n) for printing
  
Space Complexity:  
- For a singly linkedlist the space complexity is O(n)