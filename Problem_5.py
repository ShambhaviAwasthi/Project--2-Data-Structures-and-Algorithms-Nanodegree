#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Shambhavi Awasthi
# Data Structures and Algorithms NanoDegree Program
# Project 2 - Show me Data Structures
# Problem 5 - Blockchain

import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append_list(self,timestamp,data):
        if self.head is None:
            self.head=Block(timestamp,data,0)
            self.tail=self.head
        else:
            temporary_variable=self.tail
            self.tail=Block(timestamp,data,temporary_variable)
            self.tail.previous_hash=temporary_variable
            
# TEST CASES:

data="California"
timestamp="12:13 11/07/19"
block0=Block(timestamp,data,0)
block1=Block("11:15 11/02/20","Texas",block0)
print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)
temp=LinkedList()
temp.append_list(block0,"California")
temp.append_list(block1,"Texas")
print(temp.tail.data)
print(temp.tail.previous_hash.data)
block2=Block("1:02 19/12/19","Toronto",block1)
print(block1.data)
print(block1.hash)
print(block1.timestamp)
print(block2.previous_hash.data)
temp.append_list(block2,"Toronto")
print(temp.tail.data)
print(temp.tail.previous_hash.data)

data="California"
timestamp="12:13 11/07/19"      # with same timestamp
block0=Block(timestamp,data,0)
block1=Block("12:13 11/07/19","Texas",block0)
print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)

# empty block

data=""
timestamp=""      # with same timestamp
block4=Block(timestamp,data,0)
block5=Block("","",block4)
print(block4.data)
print(block4.hash)
print(block4.timestamp)
print(block5.previous_hash.data)


"""""
OUTPUT:
California
a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
12:13 11/07/19
California
Texas
California
Texas
a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
11:15 11/02/20
Texas
Toronto
Texas
California
a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
12:13 11/07/19
California

a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10


"""""






# In[ ]:




