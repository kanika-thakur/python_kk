#access list item 
list=[12,3,45,6,7,7]

#access first item
print(list[0])

#access forth item 
print(list[-2])

#change list item
list[-3]=56
print(list)

#replacing the value(3 to 78)
list[1]=78
print(list)

#append the item (adding items)
list.append(45)
print(list)

#insert the value (insert items)
list.insert(2,"apple") #2 is the index value
print(list)

#extend the value(extend means join the two lists in one lists)
list2=[12,34,5,6,7,8,8]
list.extend(list2)
print(list)

#remove items from a list
list.remove("apple")
print(list)

#clear list
list.clear()
print(list)


#basic programs of list

#maximum of two numbers
list=[12,3,45,6,7,7]
list2=[12,34,5,6,7,8,8]
print(max(list,list2))

#minimum of two lists
print(min(list,list2))

#length of numbers
print(len(list))

#reversing a list
list.reverse()
print(list)

#cloning or copying a list
list.copy()
print(list)

#Check if element exists in list
if 45 in list:
    print("elements exists in the list")
else:
    print("elements does not exists!!")

#find sum  and average in the list 
sum=sum(list)
print("the sum is:",sum)
avg=sum/6
print("the average is:",avg)


#interchange first  and last elements
list[1],list[2]=list[2],list[1]
print("list after swapping  first and last elements!!",list)

#multiply all the numbers in the list
res=1
for val in list:
    res=res*val
    print(res)

#smallest number in a list
smallest=min(list)
print(smallest)

#largest number in a list
largest=max(list)
print(largest)

#negative indexing
print(list[-3])

#range of indexing
print(list[3:6])