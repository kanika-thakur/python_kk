#try to make a marksheet 
"""print("KANIKA THAKUR")

marks1=eval(input("math marks:"))
marks2=eval(input("english marks:"))
marks3=eval(input("science marks:"))

print("marks of english is",str(marks1))
print("marks of math is",str(marks2))
print("marks of science is",str(marks3))

sum=marks1+marks2+marks3
print(" total marks  is",str(sum))

per=sum/300*100
print("percentage is",str(per))

if(per>=80):
    print("grade=A+")
elif(per<80) and  (per>=70):
    print("grade A")
elif(per<60) and  (per>=50):
    print("grade C")
else:
    print("FAIL")

#even  or odd number 
num1=eval(input("enter the number:"))
if(num1%2==0):
    print("it is a even number")
else:
    print("it is a odd number")


#ROCK-PAPER-SCISSORS
import random

options=["Rock","Paper","Scissor"]
print(options)

userChoice=input("choose: rock, paper or scissor :")
computerChoice=random.choice(options)

print("you choose:",userChoice)
print("computer choose:",computerChoice)

if(userChoice==computerChoice):
   print("it's a  tie")
elif(userChoice=="rock") and (computerChoice=="scissors"):
  print(" congrates!! YOU WIN")
elif(userChoice=="scissors") and (computerChoice=="paper"):
   print("congrates!! YOU WIN")
elif(userChoice=="paper") and (computerChoice=="rock"):
   print("congrates!! YOU WIN")
else:
   print(" sorry..COMPUTER WIN!!")"""





#check the chracter is vowel or not->
char=input("Enter the chracters:")
if char in ("a","e","i","o","u") or ("A","E","I","O","U"):
    print("IT IS A VOWEL ")
else:
    print("NOT VOWEL")


#integer number->
num= eval(input("enter the integer:"))
print(num)

if (num%2!=0):
    print("Weired")
elif(num%2==0) and (10< num <20):
    print("not weired")
elif(num%2==0) and (num>20):
    print("weired")
else:
    print("not weired ")


# #calculate the electricity bill->
bill=eval(input("Enter the units :"))
print(bill)
totalBill=bill*5
totalBill2=bill*10


if(bill<=100):
    print("NO CHARGES")
elif (100<bill<200):
   print("Rs5 per unit")
   print(totalBill)
else:
    print("Rs10 per unit")
    print(totalBill2)
 

#convert the tempreature in celsiuis and Fahrenheit->
tempF=eval(input("tempreature is:"))
print(tempF)

#formulaC=(tempF-32)//1.8
tempC=(tempF-32)//1.8
print(tempC)

#tempC=eval(input("Enter the tempreature in celsius :"))
# print(tempC)

print("celsius is",tempC)
formulaC=(tempC*1.8)+32
print(formulaC)

#print 1 to 20
num1=eval(input("Enter the number:"))
while(num1<21):
    print(num1)
    num1=num1+1
    break

