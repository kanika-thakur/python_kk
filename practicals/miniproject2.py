#A.DATATYPES AND VARIABLES=>
#1. Create a program to take input from the user and age and print greetings:
'''userInput=str(input("Enter Name:"))
userAge=input("Enter Age:")

print("GOOD MORNING!")
print(userInput)
print(userAge)
#2.create a prgram that swap two numbers without using variable:
num1=input("Enter first number:")
num2=input("Enter secound number:")

print("Before swapping num1 is:",num1,"and num2 is:",num2)

num1,num2=num2,num1

print("After swapping num1 is :",num1,"and num2:",num2)


#3.given a  list of integers ,returns  a unique number:
int=[1,2,3,45,67,6,8]
newList=set(int)
print(newList)


#4.count how many times each chracter  appears in a string:
str="this is very simple string"
print(str)

chracter_to_count=input("ENter the chracter:")
count=str.count(chracter_to_count)
print(count)

#5.Convert tuple into dictionary:
tup=(("a",4),("b",5),("g",7),("j",8))
new= dict(tup)
print(new)

#6.create a program to merge two dictionary:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print("before swapping",dict1,"and",dict2)
dict1.update(dict2)
print(dict1)



#7. write a program to remove duplicate values from a list using a set:
list1=(1,2,3,4,5,6,5,67,6)
removeVal=list(set(list1))

print(removeVal)
#8.conert a string to a list of  chracters and back to a string:
str2="chracters" 
newList=list(str2)
print(newList)

print(str2)

#9.write a program to  check if a key exists in dictionary:
fruitDict={
    "apple":2,
    "banana":5,
    "litchi":4 
}

if "mango" in fruitDict:
    print("yes it exist")
else:
    print("it doesn't exists")'''

#10. find the maximum and minimum value in a list:
list1=[1,2,3,4,5,6,7,8]


