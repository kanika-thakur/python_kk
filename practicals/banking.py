class BankAc():
    def __init__(self, acholder, acnumber, branch, type_of_ac, balance):
        self.accname = acholder
        self.accnumber = acnumber
        self.branch = branch
        self.type = type_of_ac
        self.balance = int(balance) 

    def deposit(self, amount):
     if amount < 100000:
        self.balance += amount
        print(f"Deposit successful: ₹{amount}, New Balance: ₹{self.balance}")
        print("Note: Amount deposited is less than ₹1,00,000. A transaction limit may apply.")
     else:
        self.balance += amount
        print(f"Deposit successful: ₹{amount}, New Balance: ₹{self.balance}")


    def withdraw(self,amount):
        if self.balance >= amount and amount <= 200000:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}, New Balance: ₹{self.balance}")
        else:
            print("Insufficient balance or amount exceeds ₹2,00,000 withdrawal limit.")

    def display(self):
        print(f" NEW Balance: {self.balance}")

        


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

val = BankAc(acname, acnumber, branch, type_of_ac, balance_input)

while True:
    print("1.deposit money")
    print("2.withdraw money")
    print("3.display amount")
    print("4.exit")
    choice=input("Enter the  value you want to do(1-4): ")
    if (choice=='1'):
        amount=int(input("Enter Amount you want to deposit:"))
        val.deposit(amount)
    elif(choice=='2'):
        amount=int(input("Enter Amount you want to withdraw:"))
        val.withdraw(amount)
    elif(choice=='3'):
        val.display()
    elif(choice=='4'):
        print("Exit")
        break
    else:
        print("invalid choice ! please enter choices 1 to 4:")
        


    val.display()
