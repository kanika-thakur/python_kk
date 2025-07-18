#while loop 
#1.print 10 natural numbers
''''print("NATURAL NUMBERS:")
i=1
while(i<11):
    print(i)
    i=i+1
    


#2. print even number till 10
print("EVEN NUMBERS:")
i=0
while(i<10):
    print(i)
    i=i+2

#3.print odd numbers till 10
print("ODD NUMBERS:")
i=1
while(i<10):
    print(i)
    i=i+2

#2. print even number in reverse order
print("EVEN NUMBER IN REVERSE ORDER FROM 10:")
i=10
while(i>1):
    print(i)
    i=i-2

#3. print odd number in reverse order
print("ODD NUMBER IN REVERSE ORDER FROM 10:")
i=11
while(i>0): 
    print(i)
    i=i-2

#4.print 10 integers and its squares
i=0
while(i<10):
    i=i+1
    n=i*i
    print(i,n)
    continue
i=10

#5.print the series like 10,20,30..100
print("PRINT THE SERIES upto 100:")
i=10
while(i<110):
    print(i)
    i=i+10

#6.print the following series:105,98,.....7
print("Print the following series:105,98,.....7:")
i=105
while(i>1):
    print(i)
    i=i-7

#7.print 10 natural number in reverse order 
print("Print 10 natural number in reverse order:")
i=10
while(i>0):
    print(i)
    i=i-1

#8.sum of first 10 natural numbers>>
num=10
sum=0
while(num>=1):
    sum=sum+1
    num=num-1
    print(sum )

#9.print the table of number entered ny the user
i=1
num=eval(input("ENTER THE NUMBER :"))
print("TABLE OF THE ",num)
while(i<10):
    print(num,"*",i,"=", num*i)
    i=i+1

#10.print all even numbers that falls between the numbers entered by the user:
num1=eval(input("ENTER THE NUMBER :"))
num2=eval(input("ENTER THE NUMBER :"))
if(num1>num2):
    while(num1>num2):
          if(num1%2==0):
            print(num2)
    num2=num2+1
else:
    while(num1>num2):
        if(num2%2==0):
            print(num1)
    num1=num1+1
    num1=num2+2


    


#11.factorial number:
num=int(input("ENTER THE NUMBER:"))
f=1
i=1
while(i<=num):
    f=f*i
    i=i+1
print("factorial number is:",f)'''

# #forloop =>
# for x in "bannana":
#     print(x)

# fruits=["apple","banana","cherry"]
# for x in fruits:
#     print(x)

#1.print a number 1 to 10 using while loop:
# num1=1
# while(num1<=10):
#     print(num1)
#     num1=num1+1
    

#2. print all even numbers 1 to 100:
# for i in range (0,102,2):
#     print(i)

#3.print the multiplication table of a given number:
#using a for loop=>
# for i in range (0,55,5):
#     print(i)

# Using a while loop=>
# givenNum=5
# i=1
# while(i<10):
#     print(givenNum,"*",i,"=",givenNum*i)
#     i=i+1

#4.find the sum of all numbers 1 to N :
# n = int(input("Enter a number: "))
# total = n * (n + 1) // 2
# print("Sum is:", total)

#5. calculate the factorial of the number:
# num=5
# f=1
# i=1
# while(i<num):
#     f=f*i
#     i=i+1
# print("factorial  is:",f)

#6.print the reverse of a given string using a loop:
# givenStr="kanika thakur"
# print(givenStr)


#7.count the  all digits of a number:
num=345
print(len(num))
    