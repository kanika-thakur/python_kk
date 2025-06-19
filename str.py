str="kanika thakur"
print(str)

#for find the length of string 
print(len(str))

#Convert String to Set--------
set_str=set(str)
print(set_str)

#Convert Set to String
set={1,2,3,6,7,9}
str8=str(set)
print(str8)
print(type(str8),str8)


#for reversing the string 
print(str[::-1])

#for remove first word from the string
print(str[1::])

#for remove any word from the string
print(str.replace("i"," "))

#for reversing the string to leave the one-one word
print(str[::-2])

#for find the index of string
print(str[5])

#slicing the string
print(str[1:4])

#slicing the string in negative index
print(str[-3:-1])

#for avoid the space
print(str.replace(" ",""))

#for uppercase of string
print(str.upper())

#for lowercase of string
print(str.lower())

#for finfing the text 
print(str.find('a'))

#for replacing
print(str.replace('i','o'))



#split and join a string 
str1=str.split()
str2="+".join(str1)
print(str1)
print(str2)
#index  of the chracter remove--------
i=4
res=str[:i] +str[i+1:]
print(res)

#convert string to int
s="20"
num=int(s)
print(num)

#convert integer to string
num2=str(s)
print(num2)

#split string into chracters....split means space between chracters
split=list(str)
print(split)

#to convert a string to list
res=''.join(str)
print(str)

#how to remove a letter from a string
s=str.replace("i","")
print(s)

#String is Empty or Not -------
s=""
if(s==""):
    print("THE STRING IS EMPTY")
else:
    print("THE STRING IS NOT EMPTY")



#Convert Object to String 
int=5
list=[12,23,56,"hello"]
str5=str(int)
print(str5)
print(type(str5))

str6=str(list)
print(str6)
print(type(str6))


#convert a list of chracters into chracters
list = ['k', 'a', 'n', 'i', 'k', 'a']
str4=''.join(list)
print(str4)

#sort a list of strings
list.sort()
print(list) 

#Convert tuple to string---------
tup={'red','white','blue','yellow','green'}
res=' '.join(tup)
print(res)


#formatting
str="kanika thakur"
print(str)
str10="welcome to our python programming !!"
print(str+','+str10)
formatted=f"the string is {str} and{str10}"
print(formatted)
formatted="the string is {} and {} .format(str,str10)"
print(formatted)
formatted=f"the string is %s and %s %d %(str,str10)"


#escape used in this string 
ques='what\'s up ? '
print(ques)

#list and touples
fruitList=["apple","cherry","peach","mango"]
print(fruitList)
print(len(fruitList))
print(fruitList[1])
print(fruitList[0:2])

if"apple" in fruitList:
    print("yes")












