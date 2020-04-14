# Data Structures and Algorithms Nanodegree  
## Project 3- Problems vs Algorithms
### Problem 5- Autocomplete with Tries
  
  
- find method finds corresponding nodes with given prefix
- find_suffixes uses the nodes returned by find method as input
- Used recursion to find suffixes  
  
Time Complexity-   
- To find prefix nodes, the algorithm traverses entire trie. In finding suffixes, it then loops over nested elements in the trie.
- Thus, time complexity- O(n)
  
Space Complexity-  
- Worst case space complexity- O(n)- where n is total number of characters in words, in case of no subwords