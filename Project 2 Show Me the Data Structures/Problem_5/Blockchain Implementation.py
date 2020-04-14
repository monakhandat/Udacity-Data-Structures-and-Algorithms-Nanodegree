#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
class Node:
    """
    Declaring Node for LinkedList
    """
    def __init__(self, timestamp, data, previous_hash):
        self.block = Block(timestamp, data, previous_hash)
        self.next = None
    
    def __str__(self):
        """
        Formatting print function to print entire block
        """
        output = 'Block(Timestamp='+str(self.block.timestamp)
        output += ', Data='+str(self.block.data)
        output += ', Previous hash='+str(self.block.previous_hash)
        output += ', hash='+str(self.block.hash)+')'+'\n'
        return output
    
class LinkedList:
    """
    Custom LinkedList declaration for blockchain
    """
    def __init__(self):
        self.head = None
        
    def append(self, timestamp, data):
        """
        The next block in Blockchain is 
        linked to its previous block
        i.e., previous_hash of next block/node is 
        current block/node
        """
        if self.head is None:
            self.head = Node(timestamp, data, 0)
            return
        
        # Move to the tail (the last node)
        node = self.head
        
        while node.next:
            node = node.next
        previous_hash = node.block.hash
        node.next = Node(timestamp, data, previous_hash)
        return
    
linked_list = LinkedList()
linked_list.append("12:12 2019-12-12","Some information")
linked_list.append("12:13 2020-03-12","Extra information ")
linked_list.append("12:14 2020-03-03","Extra information that I like")
node = linked_list.head

    
def test_function_1(linked_list):
    """
    checks if previous_hash of next node
    is equal to hash of current node
    """
    node = linked_list.head
    print("TEST CASE 1:")
    while node.next:
        next_node = node.next
        
        if next_node.block.previous_hash != node.block.hash:
            print("Failed Test Case 1")
            return "Fail"
        node = node.next
    print("Passed Test Case 1")
    return "Pass"

def test_function_2(linked_list):
    """
    Prints the blocks in blockchain,
    checks if traversal from node is implemented properly
    """
    node = linked_list.head
    print("-"*100)
    print("TEST CASE 2:")
    while node:
        print(node)
        node = node.next
    if node:
        print("Failed Test Case 2")
        return "Fail"
    else:
        print("Passed Test Case 2")
        return "Pass"
    

def test_function_3():
    """
    What if the linkedlist is empty
    """
    print("-"*100)
    print("TEST CASE 3")
    linked_list = LinkedList()
    node = linked_list.head
    if node:
        print("Failed Test Case 3")
        return "Fail"
    else:
        print("Passed Test Case 3")
        return "Pass"
    

test_function_1(linked_list)
test_function_2(linked_list)
test_function_3()


