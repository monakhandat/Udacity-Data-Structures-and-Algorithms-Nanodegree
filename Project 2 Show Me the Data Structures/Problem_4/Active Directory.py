#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# Adding various groups, sub-groups and users
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent_user = "parent_user"
parent.add_user(parent_user)

sub_parent = Group("subparent")
sub_parent_user = "sub_parent_user"
parent.add_group(sub_parent)

child.add_group(sub_child)
parent.add_group(child)

def re_is_user_in_group(groups_in_given_group,users_from_group):
    """
    Recursive helper function for is_user_in_group,
    checks for user in nested groups
    """
    for group in groups_in_given_group:
        users_from_group.append(group.get_users())
        check_further_groups = group.get_groups()
        if check_further_groups:
            users_from_group = re_is_user_in_group(check_further_groups,users_from_group)
    return users_from_group

def get_flat_list(users_from_group):
    """
    Get a flat list from nested list
    """
    flat_list = []
    for elem in users_from_group:
        if isinstance(elem, list):
            flat_list.extend(get_flat_list(elem))
        else:
            flat_list.append(elem)    
 
    return flat_list

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    users_from_group = []
    
    users_from_group.append(group.get_users())
    groups_in_given_group = group.get_groups()
    
    users_from_group = re_is_user_in_group(groups_in_given_group,users_from_group)
    users_flat_list = get_flat_list(users_from_group)
    
    return user in users_flat_list

# Test Case 1
print("TEST CASE 1:")
print(is_user_in_group('sub_child_user',child)) # Expected output- True
print("-"*100)

# Test Case 2
print("TEST CASE 2:")
print(is_user_in_group('parent_user',child)) # Expected output- False
print("-"*100)


# Test Case 3
print("TEST CASE 3:")
print(is_user_in_group('parent_user1',parent)) # Expected output- False
print("-"*100)

   
    

