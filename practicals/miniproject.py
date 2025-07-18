#ASSIGNMENT FOR MONDAY=>
#A.
#1.create a program that takes a user's name and age and prints greetings:
userName=str(input("Enter the Name:"))
age=eval(input("AGE:"))
print("GOOD AFTERNOON")
print(userName)
print(age)

#2. create a program that swap two numbers without using a temproary variable:
num1=input("Enter the number one:")
num2=input("Enter the number two:")
print("before swapping num1:",num1,"and num2:",num2)
num1,num2=num2,num1
print("after swapping  num1:",num1,"and num2:",num2)

#3.given a list of integers, returns a unique elements:
list=[1,2,3,4,5,5,6,7,7,8,]
new=set(list)
print(new)


#4.count how many times each chracter appears in a string:====>

#5.convert a touple into dictionary:
tup=[("a" ,1),("b",2),("c",3),("d",4)]
new=dict(tup)
print(new)
 
#6. create a program to merge two dictionary :
dict1={
    "name":"kanika",
    "age":20,
    "skinColor":"brown"
}
dict2={
    "name":"komal",
    "age":19,
    "skinColor":"white"
}
dict1.update(dict2)
print(dict1)


#7. write a program to remove duplicate values from a list using sets:
a = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(a))
print(unique_list)

#8.convert a string to a list of chracters and back to a string:
str1="red,green,blue"
list=list(str1)
print(list)

string=str(list)
print(string)


#9.write a function to check if a key exists in a dictionary:
fruit1={
    "fruitName":"apple",
    "color":"red"
}
print(fruit1)
if "fruitName" in fruit1:
    print("fruitName","exits in ",fruit1)


#10. find the maximum and minimum values in a list:
l=eval(input("Enter a list of numbers:"))
larg = l[0] 
small =l[0] 
for num in l:
    if num > larg:
        larg = num
    if num < small:
        smallest = num

print("Largest:", larg) 
print("Smallest:", small)
  





#c. CONDITIONAL STATEMENT=>

#1. check if number is positive, negative or zero :
userNum=eval(input("Enter the number:"))
if(userNum<0):
    print("NEGATIVE NUMBER..")
elif(userNum>0):
    print("POSITIVE NUMBER..")
elif(userNum==0):
    print("ZERO.")
else:
    print("ERROR!!")

#2.create a login system using if-else:
print(" Type 1 for CREATE USER &  Type 2 for LOGIN : ")
choice=int(input( "ENTER NUMBER:"))

if(choice==1):
    fName=str(input("FIRSTNAME:"))
    lName=str(input("LASTNAME:"))
    username=fName +" "+ lName
    
    print("USERNAME:",username)
    setPass=str(input("PASSWORD:"))
    confirmPass=str(input(" CONFIRM PASSWORD:"))
    if (setPass==confirmPass):
        print(" congretulations ! your profile is done . now you can login if u want.")
        print("Type 2 for LOGIN and Type 3 for exit:")
        choice=int(input( "ENTER NUMBER:"))
        if(choice==2):
            print("LOGIN")
            userName=str(input("USERNAME:"))
            passWord=str(input("PASSWORD:"))
            if(passWord==confirmPass):
                print("LOGIN SUCCCESSFUL !")
            else:
                print("WRONG PASSWORD!")
            
        elif(choice==3):
            print("EXITING!!")

    else:
        print(" SORRY! wrong password , please type again...")

elif(choice==2):
    print("LOGIN")
    userName=str(input("USERNAME:"))
    passWord=str(input("PASSWORD:"))
    print("LOGIN SUCCCESSFUL !")

else:
    print("failed!")

#3.find the largest of three numbers:
num1=eval(input("NUMBER one ="))
num2=eval(input("NUMBER two ="))
num3=eval(input("NUMBER three ="))

if(num1>num2) and (num1>num3):
    print(" LARGEST NO .:", num1)
elif(num2>num1) and (num2>num3):
    print("LARGEST NO. :", num2)
else:
    print("LARGEST NO. :",num3)

#4. check if a year is a leap year:
year=eval(input("ENTER THE CURRENT YEAR:"))

if((year%4==0) or (year%100==0) or (year%400==0) ):
    print("yes! It is a Leap year.")
else:
    print("It is not Leap year.")

#5. write a program to convert with options for celsius <-> fahrenheit:
tempF=eval(input("fahrenheit:"))

formulaC=(tempF-32)//1.8
print("fahrenheit converted into celsius:",formulaC)

print("Celsius is:", formulaC)
formulaF=(formulaC*1.8)+32
print("Celsius is converted into fahrenheit:",formulaF)


#6. find the even or odd numbers in given number:
num=3
if(num%2==0):
    print("EVEN NUMBER:",num)
else:
    print("ODD NUMBER:",num)


#7. categorize age group based on user input (child,adult, senior):
userAge=eval(input("Enter age:"))

if(userAge<18):
    print("child")
elif(userAge==18):
    print("adult")
else:
    print("senior")

#8. check if a chracter is a vowel or consonent:
char=input("Enter chracter:")

if char in (("a","i","e","o","u") or ("A","E","I","O","U")):
    print("Charcter is Vowel")
else:
    print("Chracter is Consonent")

#9.implement  a traffic light simulator(red,yellow,green)====
lightColor="RED , GREEN , YELLOW"
print("TRAFFIC-COLORS: ",lightColor)

choice=input("Enter color from TRAFFIC-COLORS:")
if(choice=="RED") or (choice=="red"):
    print("STOP")
elif(choice=="green") or (choice=="GREEN"):
    print("Go")
elif(choice=="yellow") or (choice=="YELLOW"):
    print("Slow Down")
else:
    print("ERROR!! , its not a traffic light color")

    


#10.check a wheather number is prime using conditional statements:====
num=input("ENTER NUMBER:")

if((num%1==0) or (num%num==0)):
    print("PRIME NUMBER")
else:
    print("NOT PRIME NUMBER")

#B.OPERATOR=>
#1.Write a calculator program that performs addition,subtraction,multiplication and modulo:
choice="Y"
while(choice=="Y") or (choice=="y"):
    num1=input("Enter the number one:")
    num2=input("Enter the number two:")
    operator=input("Enter the operator:")
    if(operator=="+"):
        print("RESULT:",num1+num2)
    elif(operator=="*"):
        print("RESULT:", num1*num2)
    elif(operator=="%"):
        print("RESULT:",num1%num2)
    elif(operator=="-"):
        print("RESULT:",num1-num2)
    elif(operator=="/"):
        print("RESULT:",num1/num2)
    else:
        print("ERROR!")

    choice=str(input("Do you want to continue then type Y and otherwise N and other..."))

if(choice=="Y") or (choice=="y"):
    print("continue")
else:
    print("THANKS...")


#2.check if a number is divisible by both 3 and 5:====>
num=input("Enter Number:")

if(num%3==0)and (num%5==0):
    print("Number is divisble by 3 and 5", num)
else:
    print("Number is not divisible by 3 and 5 ", num)


#3.compare two numbers and print the larger one :
num1=input("ENTER THE NUMBER1:")
num2=input("ENTER THE NUMBER2:")
if(num1>=num2):
    print("number1",num2," is larger!")
elif(num1<=num2):
    print("number2",num2,"is larger!!")
else:
    print("ERROR!!")

#4.check if a given number is even and greater than 100:
givenNum=20
if(givenNum%2==0):
     print(givenNum,"is a EVEN number and greater than 100")
elif(givenNum!=0):
     print(givenNum,"is a ODD number")
else:
    print("ERROR!")

#5.use logical operator to verify if a student passed (marks>33 and attendence>75%):
marks=input("ENTER MARKS:")
attendence=input("ENTER ATTENDENCE:")
if(marks>33) and (attendence>75):
    print("STUDENT PASSED")
else:
    print("STUDENT FAILED")
    
#6.use commpaound assignment operator (+=,-=)  to update  a score variable:
num=45



#7.demonstarta short circuitng withh logical operator:
num=1
while(num>10):
    print(num)
    break
num==3
num2=4
while(num2>10):
    print(num2)
    break
num==8
num3=9
while(num3>12):
    print(num3)
#LOOP=>
#1.print all the numebrs from 1 to 100:

num=1
while(num<=100):
    print(num)
    num=num+1

#2.multiplication table of a given number:
i=1
givenNum=5
print("table of number:",givenNum)
while(i<10):
      print(givenNum ,"*", i,"=",givenNum * i ) 
      i=i+1

#3.calculator the factorial of a number:
num=5
f=1
i=1
while(i<=num):
      f=f*i
      i=i+1
print("factorial number is :",f)

#4.print the fabonacii series :
n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()

#5.find the sum of a digits of a number:
n = int(input("Enter the value: "))
result = sum(int(digit) for digit in str(n))
print("The output will be: ",result)

#6.reverse a given string using a loop :
str="My name is Kanika Thakur"
rev=str[::-1]
print(rev)

#7.count the number of vowels in a string:
string=str("Enter string:")
count=0
string=string.lower()
for i in str:
    if(i == "a","A") or (i=="e","E")or(i=="o","O") or (i=="u","U") or (i=="i","U"):
        count+=1
if (count==0):
    print("NO vowels found !!")
else:
    print("Total vowels are :", + str(count))

    
#8. create a pattern using nested loops:
rows = 5  
for i in range(1, rows + 1):  
    for j in range(i):  
        print("*", end=" ") 
    print()

#9. check wheather a number is an armstrong number:
num = 1168
num_str = str(num)
num_len = len(num_str)
armstrong_sum = sum([int(digit) ** num_len for digit in num_str])

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.") 


#10. use a while loop to find the first 10 prime number:


