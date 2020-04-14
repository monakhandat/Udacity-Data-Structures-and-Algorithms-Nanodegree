# Data Structures and Algorithms Nanodegree
## Project 2- Show Me the Data Structures
### Problem 3- Huffman Coding

- The data structure used for Huffman Coding- heapq- priority heap
- Huffman coding is a complex problem and things get even complex if tried using lists
- I thought of two options initially- list with namedtuples and heapq.
- I faced hard time in building tree stage with namedtuples, hence I tried using heapq
- The inbuilt methods- heappush and heappop simplified the tree building process
- Each element in the heapq is a HuffmanNode that helped in defining comparison parameter. The comparison parameter was needed to establish priorities between characters(nodes) for heappush and heappop.
- Recursion is used to traverse the HuffmanTree to create binary code for each of the character in given sentence. Recursion is also used in decoding the encoded data.
  
  
Time Complexity-
- O(log n) in each iteration to insert a Huffman node in heapq and O(n) for each of the iteration.
- The complexity of Huffman coding is O(nlogn)
  
Space Complexity-
- O(# of unique characters in given data)