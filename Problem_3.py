#!/usr/bin/env python
# coding: utf-8

# In[7]:



# Shambhavi Awasthi
# Data Structures and Algorithms NanoDegree Program
# Project 2 - Show me Data Structures
# Problem 3 - Huffman Coding
"""
ALGORITHM:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.

"""

import sys
global huff

def encoding(data): # encoding huffman function
    global huff 
    huff = {}
    tree = {}
    temp = '1'
    for char in data:
        huff[char] = huff.get(char, 0) + 1
    for num in sorted(huff.items(), key = lambda x: x[1]):
        tree[num[0]] = temp
        temp = '0' + temp
    encode = ''
    for d in data:
        encode += tree[d]
    return encode, tree

def decoding(data,tree):
    huff = {}
    for char in tree:
        huff[tree[char]] = char
    temp = ''
    decode = ''
    for d in data:
        if d == '1':
            decode += huff[temp + d]
            temp = ''
        else:
            temp += d
    return decode

# Test case 1:
print("TEST CASE 1")
if __name__ == "__main__":
    codes = {}
    sentence = "Hello my name is Shambhavi"
    encoded_data, tree = encoding(sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The encoded data is: {}".format(encoded_data))
    decoded_data = decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The decoded data is: {}\n".format(decoded_data))
    
    
    # Test case 2:
print("TEST CASE 2")
if __name__ == "__main__":
    codes = {}
    sentence = ""
    if(sentence == ""):
        print("No data to encode\n")
    else:
        encoded_data, tree = encoding(sentence)
        print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}".format(encoded_data))
        decoded_data = decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
        print ("The decoded data is: {}\n".format(decoded_data))

    
    # Test case 3:
print("TEST CASE 3")   
if __name__ == "__main__":
    codes = {}
    sentence = "eeeeeeeeeeeeeeeeeeeee"
    encoded_data, tree = encoding(sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The encoded data is: {}".format(encoded_data))
    decoded_data = decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The decoded data is: {}".format(decoded_data))
    
    
    
    """
    OUTPUT:
    
TESTCASE 1:
    
The size of the data is: 75

The content of the data is: Hello my name is Shambhavi

The size of the encoded data is: 60

The content of the encoded data is: 100000000100000000010000000001010000000000000010000000000001001000000000000001000100000000000001000000000000100000000100000000000000100000000001000010000000000000010000010000000000010000000000000100000000000010000001000000000001000000000000010000000100000000001

The size of the decoded data is: 75

The content of the decoded data is: Hello my name is Shambhavi


TESTCASE 2:

No data to encode


TESTCASE 3:

The size of the encoded data is: 28
The encoded data is: 111111111111111111111
The size of the decoded data is: 70
The decoded data is: eeeeeeeeeeeeeeeeeeeee


"""
    







# In[ ]:




