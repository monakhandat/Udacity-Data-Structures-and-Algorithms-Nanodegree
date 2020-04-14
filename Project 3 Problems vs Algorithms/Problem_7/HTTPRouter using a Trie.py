#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import defaultdict

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,not_found_handler):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = not_found_handler

    def insert(self, char):
        # Insert the node as before
        self.children.append(char)
        
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler,not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(not_found_handler)
        self.handler = handler
        self.default_handler = not_found_handler

    def insert(self, value, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        #handler_value = ''
        current_node = self.root
        #value_list = value.split("/")
        for val in value:
            #if val not in current_node.children:
            if not current_node.children.get(val):
                current_node.children[val] = RouteTrieNode(self.default_handler)
                #handler_value += val + " "
            current_node = current_node.children[val]

        current_node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        current_node = self.root
        
        for val in path_list:
            if not current_node.children.get(val) :
                return self.default_handler
            current_node = current_node.children[val]
        
        if current_node.handler:
            return current_node.handler
        else:
            return None
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler,not_found_handler)
       

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        current_node = self.root
    
        current_node.insert(self.split_path(path),handler)
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        current_node = self.root
        path_list = self.split_path(path)
        if path_list:
            return current_node.find(path_list)
        else:
            return current_node.handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split("/")
        path_list = list(filter(None, path_list))
        return path_list
                



# create the router and add a route
router = Router("root handler","not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' 
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' 
print(router.lookup("/home/about/me")) # should print 'not found handler'         

