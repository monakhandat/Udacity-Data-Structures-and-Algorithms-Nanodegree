#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
import sys
from collections import Counter
class Huffman_Node:
    """
    Nodes are defined to create Huffman tree out of each character, frequency tuple
    Each of the node has left and right nodes
    """
    def __init__(self,character, frequency):
        
        self.left = None
        self.right = None
        self.character = character
        self.frequency = frequency        
        
    def __lt__(self, other):
        """
        Nodes are compared using frequency
        """
        return self.frequency < other.frequency

def get_frequency(data):
    """
    Function accepts the string as input and gives Huffman nodes of each character
    sorted in ascending order by the frequency
    """
    frequency_per_char = Counter(data)
    sorted_freq =  sorted(frequency_per_char.items(), key=lambda pair: pair[1], reverse=False)
    freq_sorted_nodes =[Huffman_Node(char,freq) for char, freq in sorted_freq]
    
    return freq_sorted_nodes
    
def build_tree(sorted_freq):
    """
    Building tree using frquency sorted Huffman Nodes
    i.e. creating a root node, adding left and right Huffman Nodes
    Root node is combination of left and right nodes
    value of root = both Huffman node values
    Frequency of root nodes = Addition of Huffman Node frequencies
    """
    while(len(sorted_freq)!=1):
        left_node = heapq.heappop(sorted_freq)
        right_node = heapq.heappop(sorted_freq)
        root_node = Huffman_Node(left_node.character+right_node.character, right_node.frequency+left_node.frequency)
        root_node.left = left_node
        root_node.right = right_node
        heapq.heappush(sorted_freq, root_node)
    return sorted_freq

def huffman_encoding_hashmap(huffman_tree,huffman_hashmap):
    """
    Create a hashmap table(more like a lookup table)
    The table contains each of the character as key
    and a unique binary code that represents the character in Huffman Tree built.
    This is based on traversal of binary tree
    """
    binary_code = ""
    def path_from_node_to_root(root, binary_code):
        if root is None:
            return None,""

        elif root.left is None and root.right is None:
            huffman_hashmap[root.character] = binary_code

        path_from_node_to_root(root.left,binary_code+"0") # add 0 if traversing to left node
        path_from_node_to_root(root.right,binary_code+"1") # add 1 if traversing to right node
    
    path_from_node_to_root(huffman_tree[0], binary_code)
    
    return huffman_hashmap
    

def huffman_encoding(data):
    """
    This function takes each character in data and appends
    corresponding binary code to a string called encoded_output
    Output of this function is Huffman encoded output for given data/sentence
    """
    sorted_freq = get_frequency(data)
    huffman_tree = build_tree(sorted_freq)
    huffman_hashmap = {}
    huffman_hashmap = huffman_encoding_hashmap(huffman_tree,huffman_hashmap)
    
    encoded_output=""
    for item in data:
        encoded_output+=huffman_hashmap[item]
    
    return encoded_output, huffman_tree


def huffman_decode(encoded_output, index, chara, root):
    """
    Recursive helper function for huffman_decoding
    This function traverses the Huffman tree using given encoded_output
    The function returns charcater found at the terminal node of Huffman tree
    along with index in encoded_output for new character binary code or tree traversal
    """
    if root is None:
        print("NONE")
        return index, chara
    
    elif root.left is None and root.right is None:
        chara += root.character
        return index, chara
    
    index +=1
    if encoded_output[index] is "0":
        index,chara = huffman_decode(encoded_output, index, chara, root.left)
    else:
        index,chara = huffman_decode(encoded_output, index, chara, root.right)
    
    return index, chara

def huffman_decoding(encoded_output,huffman_tree):
    """
    Returns the decoded output
    """
    index  = -1
    chara = ""
    while(index < len(encoded_output)-2):
        index,chara = huffman_decode(encoded_output, index, chara, huffman_tree[0])
 
    return chara


def test_function(data):
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    encoded_data, tree = huffman_encoding(data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    if data == decoded_data:
        print("Test Case Passed!")
    else:
        print("Fail")
    

# Test Case 1
print("="*100)
print("TEST CASE 1")
print("="*100)
test_function("The bird is the word")

# Test Case 2
# Using symbols
print("="*100)
print("TEST CASE 2")
print("="*100)
test_function("Hi There...!!!!")

# Test Case 3
# Using repeated letters
print("="*100)
print("TEST CASE 3")
print("="*100)
test_function("Mississippi is mississippi")




    

