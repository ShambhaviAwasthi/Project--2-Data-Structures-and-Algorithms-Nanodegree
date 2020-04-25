#!/usr/bin/env python
# coding: utf-8

# In[16]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree Program
# Problem 6: Union and Intersection of two Linked List Python Code


class Node:    #defining node class 
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):  # creating a node with input value
        return str(self.value)


class LinkedList: #creating class LL
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value): #adding values to the linked list

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):  #to find the size of the linked list
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    

    
    
def union(llist_1, llist_2): #function to find union with arguments as input linked list
    head_1=llist_1.head # taking a variable at the head of 1st LL
    head_2=llist_2.head #  taking a variable at the head of 1st LL
    union_set=set() # taking a set to store unique values from the two given lists
    union_ll=LinkedList() #creating a union list
    
    if llist_1.size()==0 and llist_2.size()==0: # if both are empty return None
        return None
 
    elif head_1 is None: #if LL1 is empty, return LL2
        return llist_2
    
    elif head_2 is None: #if LL2 is empty, return LL1
        return llist_1
    elif llist_1.size()==0 and llist_2.size()==0: # if both are empty return None
        return None
    else:
        while head_1 is not None: # adding all unique values from LL1 to the set
            union_set.add(head_1.value)
            head_1=head_1.next   
            
        while head_2 is not None: # adding all unique values from LL2 to same set
            union_set.add(head_2.value)
            head_2=head_2.next
            
        union_list=list(union_set) # converting set to union LL
        for i in union_list:
            union_ll.append(i)
        return union_ll
   


    
def intersection(llist_1, llist_2): # function to find intersection
    list1=[]
    list2=[]
    head1=llist_1.head   #taking head of LL1
    head2=llist_2.head   #taking head of LL2
    intersect=set()
    intersect_ll=LinkedList()
    
    while head1 is not None:
        list1.append(head1.value)
        head1=head1.next
        
    while head2 is not None:
        list2.append(head2.value)
        head2=head2.next
        
    for i in range(0,len(list1)): #taking one element form one list and searching for it in the next list while storing it in a set
        val1=list1[i]
        for j in range(0,len(list2)):
            val2=list2[j]
            if(val1==val2):
                intersect.add(val1)
    intersect_list=list(intersect)
    
    for i in intersect_list:    # convertin the set of intersection to LL
            intersect_ll.append(i)
    if intersect_ll.size()==0:
        return None
    else:
        return intersect_ll

            
        


# Test case 1

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

# Test case 2

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

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,2,3,5,6]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# Test case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [2,89,36,90,2,4,0]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test Case 5

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))





"""""OUTPUT:
32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->             TESTCASE 1
4 -> 21 -> 6 -> 
65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->   TESTCASE 2
None
1 -> 2 -> 3 -> 5 -> 6 ->                                                TESTCASE 3
None
2 -> 89 -> 36 -> 90 -> 2 -> 4 -> 0 ->                                   TESTCASE 4
None  
None                                                                    TESTCASE 5
None
"""""


# In[ ]:





# In[ ]:




