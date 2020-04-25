#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree Program
# Problem 2 - Project 2 Show me the Data Structures
# File recursion

import os

def findFiles(path, pathList,extension):
    subFolders=True
    try: 
        for entry in os.scandir(path):
            if entry.is_file() and entry.path.endswith(extension): #if entry file is found and ends with given extension
                pathList.append(entry.path) #append the path to output list
            elif entry.is_dir() and subFolders: # checking the subfolders with recursive call
                pathList = findFiles(entry.path, pathList,extension)
    except OSError:
        pathList.append("Input Path is invalid.")
    return pathList


# Test Cases: 

dir_name = r'C:\Users\Shambhavi\Downloads'
extension = ".c"

pathList=[]
pathList = findFiles(dir_name,pathList, extension)

if len(pathList)==0:
    print("No files found for the given extention")
else:
    print("The paths containing the files with .c extension are :")
    for i in range(0,len(pathList)):
        print(pathList[i])
        
# Test Case 2:

dir_name = r'D:\Users\Shambhavi\Downloads'
extension = ".c"

pathList=[]
pathList = findFiles(dir_name,pathList, extension)

if len(pathList)==0:
    print("No files found for the given extention")
else:
    print("The paths containing the files with .c extension are :")
    for i in range(0,len(pathList)):
        print(pathList[i])

        
        
# Test Case 3:

dir_name = r'C:\Users\Shambhavi\Downloads\Schneider Electric'
extension = ".c"

pathList=[]
pathList = findFiles(dir_name,pathList, extension)

if len(pathList)==0:
    print("No files found for the given extention")
else:
    print("The paths containing the files with .c extension are :")
    for i in range(0,len(pathList)):
        print(pathList[i])
        
#OUTPUTS:

#TEST CASE 1:
#The paths containing the files with .c extension are :
#C:\Users\Shambhavi\Downloads\testdir\testdir\subdir1\a.c
#C:\Users\Shambhavi\Downloads\testdir\testdir\subdir3\subsubdir1\b.c
#C:\Users\Shambhavi\Downloads\testdir\testdir\subdir5\a.c
#C:\Users\Shambhavi\Downloads\testdir\testdir\t1.c

#TEST CASE 2:
#Input Path is invalid.

#TEST CASE 3:
#No files found for the given extention





# In[ ]:




