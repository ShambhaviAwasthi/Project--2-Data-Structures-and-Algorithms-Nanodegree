#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree Program
# Problem 1 - Project 2 Show me the Data Structures
# LRU Cache


from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache_capacity=capacity
        self.cache_value={}            #using dictionary to store key,value pair
        self.cache_order= deque()      # to store the order in which elements appear to check least used.

    def get(self, key): #to get value from given key, if not found return -1
        if key is None:
            return -1
        return self.cache_value.get(key,-1) # return value

    def set(self, key, value):
        if self.cache_capacity==0:
            print("Capacity is zero")
        else:
            if len(self.cache_order) >= self.cache_capacity:   #to check if cache is full
                del self.cache_value[self.cache_order.popleft()] # the left most element is the least used element as it was entered first
            self.cache_order.append(key) # set the key in order deque
            self.cache_value[key] = value # store the cache

        
        
# test cases 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 2);
our_cache.set(4, 4);

print(our_cache.cache_value)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(None))    # return -1
print(our_cache.get(9))       # return -1 as 9 is not present

our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))

print(our_cache.get(1))     # returns -1 because the cache reached it's capacity and 1 was the least recently used entry

""""" OUTPUT:

{1: 1, 2: 2, 3: 2, 4: 4}
1
2
-1
-1
-1

"""""

# test cases 2

our_cache = LRU_Cache(0)
our_cache.set(2, 2); # output: capacity is zero

# test case 3: getting only invalid values
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
print(our_cache.get(8))  # returns -1
print(our_cache.get(9))  # returns -1
print(our_cache.get(10))  # returns -1
print(our_cache.get(11))  # returns -1


# In[ ]:




