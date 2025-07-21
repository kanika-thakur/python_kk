class BankAc():
    def __init__(self,acholder,acnumber,branch,type_of_ac,balance):
        self.accname=acholder
        self.accnumber=acnumber
        self.branch=branch
        self.type=type_of_ac
        self.balance=balance

    def deposit(self,amount):
        if(amount>100000):
            self.balance+=amount
            print(f"Deposit money:{amount}, New Balance:{self.balance}")
        else:
            print("Transaction limit set: Your balance is below ₹1,00,000")

    def withdraw(self,amount):
        if(self.balance>=amount) and (amount>200000):
            self.balance-=amount
            print(f"Withdraw money:{amount} New Balnce:{self.balance}")
        else:
            print("insufficient")

    def display(self):
        print(f"balance:,{self.balance}")


acname=input("Enter the Account Name:")
if (6<= len(str(acname))<=20):
    print("Account Holder:", acname)
else:
    print("Invalid account name!!. It should contain 6 to 20 digits")

acnumber=int(input("Enter the Account Number:"))
if  (9<= len(acnumber) <=15):
    print("Account Number:", acnumber)
else:
    print("Invalid account number: It should contain 9 to 18 digits")


allowed_branches=["SBI","PNB","CO-OPREATIVE ","HDFC","ICICI","AXIS",] or["sbi","hdfc","pnb","axis","co-operative","icici"]
branch=input("Enter Branch Name:")
if branch in allowed_branches:
    print("Account Branch:", branch)
else:
    print("Invalud Branch Name!")

allowed_typeac=["savings account","current account","salary account","fixed deposit account","recurring deposit account"] or ["SAVINGS ACCOUNT", "CURRENT ACCOUNT","SALARY ACCOUNT","FIXED DEPOSIT ACCOUNT","RECURRING DEPOSIT ACCOUNT"]
type_of_ac=input("Enter the type of Account:")
if type_of_ac in allowed_typeac:
    print("Account:",type_of_ac)
else:
    print("invalid type of account")

balance=float(input("Your Balance:"))
print("Balance:",balance)
print("    ")

print(
    f"Account Holder:{acname},"
    f"Account Name:{acnumber},"
    f"Your Branch:{branch},"
    f"Type of Account:{type_of_ac},"
    f"balance:{balance}"
)
print("  ")

val=BankAc(acname,acnumber,branch,type_of_ac,balance)
val.deposit(10)
val.withdraw(50)
val.display()
print("   ")






print("-----------------student management system----------------------")

class StudentManagement():
    def __init__(self, student_id, name, grade, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.grade = grade

    def display(self):
        print(self.student_id, self.name, self.grade, self.marks)
        return f"{self.student_id}, {self.name}, {self.grade}, {self.marks}"  #  Add return for print()
    
    def __str__(self):
      return f"{self.student_id}, {self.name}, {self.grade}, {self.marks}"


class StudentManager():
    def __init__(self):
        self.students = []

    def add(self, student_id, name, grade, marks):
        for student in self.students:
            if student.student_id == student_id:
                print("studentid already exists")
                return "add failed"  

        new_students = StudentManagement(student_id, name, grade, marks)
        self.students.append(new_students)
        print(new_students, "added successfully")
        return "Student added" 

    def update(self, student_id, name='none', grade='none', marks='none'):
        for student in self.students:
            if student.student_id == student_id:
                if name != 'none':
                    student.name = name
                if grade != 'none':
                    student.grade = grade
                if marks != 'none':
                    student.marks = marks
                print("update successfully")
                return "Update done" 

        print("student not found")
        return "Update failed: Not found" 
    def delete(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("deleted successfully")
                return "delete done"
          
            else:
                print("student not found")
                return "Delete failed: Not found" 

print("-----------------student detail----------------------")
student_id=input("Enter student_id:")
name=input("Enter your name:")
grade=input("Enter your grade:")
marks=float(input("Enter marks:"))

val = StudentManagement(student_id,name,grade,marks)
print("Student detail:", val.display())

print("-----------------add student----------------------")
val2=StudentManager()
student_id1=input("Enter student_id:")
name3=input("Enter your name:")
grade=input("Enter your grade:")
marks=float(input("Enter marks:"))
print("Add student:", val2.add(student_id1,name3,grade,marks))

print("-----------------update student----------------------")
student_id1=input("Enter student_id:")
name=input("Enter your name:")
grade1=input("Enter your grade:")
marks1=float(input("Enter marks:"))
print("Update student info:", val2.update(student_id1,name,grade1,marks1))

print("-----------------delete student----------------------")
name2=input("Enter name you want to delete:")
print("Delete student:", val2.delete(name2))


