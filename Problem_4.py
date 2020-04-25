#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Shambhavi Awasthi
# Data Structures and Algorithms NanoDegree Program
# Project 2 - Show me Data Structures
# Problem 4 - Active Directory

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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def userGroup(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    if user== group.get_name():  # if user equal first group
        return True
    if user in group.get_users(): # if user is in users list
        return True
    for grp in group.get_groups(): # if the group contains another group, call recursion
        return userGroup(user, grp)
    return False

#Test Cases
print(is_user_in_group("child", child)) #True
print(is_user_in_group("", child))  #False
print(is_user_in_group("sub_child_user", parent))   #True


# In[ ]:




