#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        output_list = []
        node = self.head
        while node is not None:
            output_list.append(node.value)
            node = node.next
        
        return output_list



def get_intersection_list(llist_1, llist_2):
    list_1 = LinkedList.to_list(llist_1)
    list_2 = LinkedList.to_list(llist_2)
    intersection_list = []
    flag = [0]*1000
    for element in list_1:
        if element in list_2:
            flag[element] += 1
            if flag[element] == 1:
                intersection_list.append(element)
            elif flag[element] > 1:
                occurence_in_list_2 = check_occurrences(list_2, element)
                if occurence_in_list_2 >= flag[element]:
                    intersection_list.append(element)
    print("Intersection list", intersection_list)
    return intersection_list

def intersection(llist_1, llist_2):
    #intersection_list = []
    intersection_list = get_intersection_list(llist_1, llist_2)
    intersection_linked_list = LinkedList()
    for element in intersection_list:
        intersection_linked_list.append(element)
    return intersection_linked_list

def check_occurrences(list_2, element):
    freq = 0
    for l in list_2:
        if l == element:
            freq += 1
    return freq

def union(llist_1, llist_2):
    # Your Solution Here
    list_1 = LinkedList.to_list(llist_1)
    list_2 = LinkedList.to_list(llist_2)
    #intersection_list = []
    intersection_list = get_intersection_list(llist_1, llist_2)
    output_list = list_1+list_2
    for i in intersection_list:
        if i in output_list:
            output_list.remove(i)
    print("Union List: ",output_list)
    
    union_linked_list = LinkedList()
    for element in output_list:
        union_linked_list.append(element)
    return union_linked_list

# Test case 1
print("TEST CASE 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

print("-"*100)

# Test case 2
print("TEST CASE 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
print("-"*100)



# Test case 3
print("TEST CASE 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [13,10,3,5,16,30,18,2,7, 4, 4]
element_2 = [3, 4, 4, 9, 10, 18, 29,30, 31,34]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

