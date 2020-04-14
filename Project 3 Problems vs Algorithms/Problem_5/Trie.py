#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children.append(char)
        
## The Trie itself containing the root node and insert/find functions


# In[2]:


class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node
    
    


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[25]:


from collections import defaultdict
class TrieNode:
    def __init__(self):
        """
        Initialize this node in the Trie
        """
        self.is_word = False
        self.children = defaultdict(TrieNode)
        
    
    def insert(self, char):
        """
        Add a child node in this Trie
        """
        self.children.append(char)
        
        
    def suffixes(self, word_list, suffix = ''):
        """
        Recursive function that collects the suffix for 
        all complete words below this point
        
        """
        temp_word = suffix
    
        if self.children:
            for (key, value) in self.children.items():
                if value.is_word:
                    word_list.append(suffix+key) 
                word_list = value.suffixes(word_list,suffix+key)
        
        return word_list
        
    
            
    def __str__(self):
        """
        Format print method
        """
        out = ''
        for ch in self.children:
            out += ch
        
        return out
            


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[26]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[35]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            word_list = []
            print('\n'.join(prefixNode.suffixes(word_list)))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')


# In[39]:


def test_function(prefix):
    prefixNode = MyTrie.find(prefix)
    if prefixNode:
        word_list = []
        print('\n'.join(prefixNode.suffixes(word_list)))
    else:
        print(prefix + " not found")
            
# Test Case 1- check for words/prefixes not in trie
test_function('g') # Expected output- g not found

# Test Case 2- enter complete word
test_function('factory') # Expected output- An empty line

# Test Case 3
test_function('f') # Expected output- un, unction, actory each on new line

