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

class BankAc():
    def __init__(self, acholder, acnumber, branch, type_of_ac, balance):
        self.accname = acholder
        self.accnumber = acnumber
        self.branch = branch
        self.type = type_of_ac
        self.balance = balance

    def deposit(self, amount):
     if amount < 100000:
        self.balance += amount
        print(f"Deposit successful: ₹{amount}, New Balance: ₹{self.balance}")
        print("Note: Amount deposited is less than ₹1,00,000. A transaction limit may apply.")
     else:
        self.balance += amount
        print(f"Deposit successful: ₹{amount}, New Balance: ₹{self.balance}")


    def withdraw(self):
        if self.balance >= amount and amount <= 200000:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}, New Balance: ₹{self.balance}")
        else:
            print("Insufficient balance or amount exceeds ₹2,00,000 withdrawal limit.")

    def display(self):
        print(f"Balance: {self.balance}")

        


# Input and Validations
acname = input("Enter the Account Name: ")
if 6 <= len(acname) <= 20:
    print("Account Holder:", acname)
else:
    print("Invalid account name! It should contain 6 to 20 characters.")

acnumber = input("Enter the Account Number: ")
if acnumber.isdigit() and 9 <= len(acnumber) <= 15:
    acnumber = int(acnumber)
    print("Account Number:", acnumber)
else:
    print("Invalid account number: It should contain 9 to 15 digits.")

allowed_branches = ["SBI", "PNB", "CO-OPERATIVE", "HDFC", "ICICI", "AXIS"]
branch = input("Enter Branch Name: ").upper()
if branch in allowed_branches:
    print("Account Branch:", branch)
else:
    print("Invalid Branch Name!")

allowed_typeac = [
    "SAVINGS ACCOUNT", 
    "CURRENT ACCOUNT",
    "SALARY ACCOUNT", 
    "FIXED DEPOSIT ACCOUNT",
    "RECURRING DEPOSIT ACCOUNT"
]
type_of_ac = input("Enter the Type of Account: ").upper()
if type_of_ac in allowed_typeac:
    print("Account Type:", type_of_ac)
else:
    print("Invalid type of account!")

balance_input = input("Enter  Balance: ")

print("\nAccount Created Successfully:")
print(f"Account Holder: {acname}")
print(f"Account Number: {acnumber}")
print(f"Branch: {branch}")
print(f"Account Type: {type_of_ac}")
print(f"Balance: { balance_input }")


# Create object and test methods
val = BankAc(acname, acnumber, branch, type_of_ac, balance_input)
amount=int(input("Enter Amount you want to deposit:"))
val.deposit(amount)

amount=int(input("Enter Amount you want to withdraw:"))
val.withdraw(amount)

val.display()+