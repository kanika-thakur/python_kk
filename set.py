#make a set
set={"Apple","bannana","litchi"}
print(set)

#length of set
print(len(set))

#type of set
print(type(set))

#we can amke a set using set() constructor
set1=(("apple","banana","mango"))
print(set1)

#access items 
for x in set:
    print(set)

#add items
set.add("orange")
print(set)

#remove items
set.remove("Apple")
print(set)

#join sets------
#by using union 
set3=set.union(set1)
print(set3)

#by using | joinb
"""set2 = set | set1
print(set2)"""

#update set
set.update(set1)
print(set)

#set emthods-----
#add element the set 
set.add("cherry")
print(set)

#remove from a list
set.remove("apple")
print(set)

#clear all values
"""set.clear()
print(set)
"""
#copy values
set.copy()
print(set)

#differce between two values
set.difference("orange","litchi")
print(set)


#pop remove elements from a lsit 
set.pop("orange")
print(set)


#
