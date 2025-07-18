#create a class=>
# class MyClass:
#     x='kanika'

# n=MyClass()
# print(n.x)


#constructor=>
#Create a class Person that stores a person's name and age. Add a method to display the details.
# class MyClass():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def show(self):
#         print("name:", self.name)
#         print("age:",self.age)
# p1=MyClass("naman",17)
# p1.show()


#Create a class Circle that calculates the area of a circle:
# class Circle():
#     def __init__(self,radius):
#         self.radius=radius
    

#     def circle(self):
#         return 3.14* self.radius*self.radius

# c1=Circle(3)
# print("area of circle:",c1.circle())

#Create a class Student that takes roll number and marks of 3 subjects and prints the total:
# class Student():
#     def __init__(self,rollno,m1,m2,m3):
#         self.rollno=rollno
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def total(self):
#         return(self.m1+self.m2+self.m3)
# t1=Student(12,34,56,78)
# print("total:", t1.total())

#Create a class Rectangle that calculates area and perimeter:
# class Rectangle():
#     def __init__(self,width,length):
#         self.width=width
#         self.length=length

#     def area(self):
#         return self.width*self.length
    
#     def parameter(self):
#         return (self.width+self.length)*2

# val=Rectangle(12,23)
# print("area of frectangle:",val.area())
# print("parameter of ractangle:",val.parameter())

#Create a class BankAccount with deposit and withdraw methods:
# class BankAccount():
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if(amount<=self.balance):
#             self.balance-=amount
#         else:
#             print("Insufficient money! ")
    
#     def show_balance(self):
#         print("balance:",self.balance)


# acc=BankAccount("kanika",10000) 
# acc.deposit(500)  
# acc.withdraw(30000)
# acc.show_balance()

# Create a class Car with attributes brand and price, and a method to display them:
# class Car():
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price

#     def show(self):
#         print("name:",self.brand)
#         print("price:",self.price)

# val=Car("maruti",10000)
# val.show()
        
#Create a class Employee with a method to calculate yearly salary:
# class Employee():
#     def __init__(self,salary):
#         self.salary=salary
    
#     def yearly_salary(self):
#         return self.salary *12
    
# p1=Employee(10000)
# print("Yearly Salary:", p1.yearly_salary())

# #Create a class BankAccount with methods deposit, withdraw, and show_balance:
# class BankAccount():
#     def __init__(self,owner,total):
#         self.owmner=owner
#         self.total=total
        
#     def deposit(self,amount):
#         self.total+=amount
    
#     def withdraw(self,amount):
#         if(self.total>amount):
#             self.total-=amount
#         else:
#             print("insufficient money!")

#     def show(self):
#         print("balance:",self.total)
    

# bal=BankAccount("kanika",100000)
# bal.deposit(1200)
# bal.withdraw(500)
# bal.show()
    
#1.marksheet=>
# class MarkSheet():
#     def __init__(self,studentName,rollno,maths,science,english,hindi):
#         self.studentName=studentName
#         self.rollno=rollno
#         self.maths=maths
#         self.science=science
#         self.english=english
#         self.hindi=hindi
#         self.sum=0
#         self.per=0


#     def total(self):
#         self.sum= self.maths+self.science+self.english+self.hindi
#         print("sum:",self.sum)
    
#     def percentage(self):
#         self.per=self.sum/4
#         print("percentage:",self.per)

#     def grade(self):
#         per=self.sum/4
#         if(per>=80):
#             print("grade A")
#         elif(per>=70):
#             print("grade B")
#         elif(per>=50):
#             print("grade C")
#         else:
#             print("FAIL")

        
# val=MarkSheet("kanika",12,56,57,89,45)
# val.total()
# val.percentage()
# val.grade()

#2.calculator:
# class Calculator():
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
       
#     def addition(self):
#         return (self.num1+self.num2)
    
#     def subtraction(self):
#         return self.num1-self.num2
    
#     def multiply(self):
#         return self.num1*self.num2
    
#     def division(self):
#         if(self.num1!=0) and (self.num2!=0):
#             return self.num1/self.num2
#         else:
#             print("cannot divide by zero")
    
#     def modules(self):
#         return self.num1%self.num2
    
#     def eqal(self):
#         if(self.num1==self.num2):
#             print("self.num1=self.num2")
#         else:
#             print("ERROR!")
    
#     def default(self):
#       return 0
    
# num1=float(input("FIRST NUMBER:"))
# num2=float(input("SECOUND NUMBER:"))
# operator=input("OPERATION:")
   
# val=Calculator(num1,num2)

# # print("ADDITION:",val.addition())
# # print("MULTIPLY:",val.multiply())
# # print("SUBTRACTION:",val.subtraction())
# # print("DIVISION:",val.division())
# # print("MODULES:",val.modules())
# # val.eqal()

# if(operator=='+'):
#     print("ADD:",val.addition())
# elif(operator=='-'):
#     print("SUBTRACT:",val.subtraction())
# elif(operator=='/'):
#     print("DIVIDE:",val.division())
# elif(operator=='%'):
#     print("Modules:",val.modules())
# elif(operator=='='):
#     print("Eqal:",val.eqal())
# else:
#     print("invalid operation selected!!")


#3.area of square:
# class Square():
#     def __init__(self,side):
#         self.side=side

#     def area(self):
#         return self.side*self.side
        

# side=float(input("Enter side of square:"))
# val=Square(side)

# print("Area of square:",val.area())

#4.student report card :
# class report_card():
#     def __init__(self,studentName,rollno,english,science,math,hindi):
#         self.studentname=studentName
#         self.rollno=rollno
#         self.hindi=hindi
#         self.english=english
#         self.math=math
#         self.science=science

#     def per(self):
#         p=(self.hindi+self.english+self.math+self.science)/4
#         print(p)
    
#     def grade(self):
#         p=(self.hindi+self.english+self.math+self.science)/4
#         if(p<=90):
#             print("A+")
#         elif(p<=80):
#             print("A")
#         elif(p<=60):
#             print("B")
#         elif(p<=50):
#             print("C")
#         else:
#             print("FAIL!!")

#     def display_result(self):
#         print("Name:",self.studentname)
#         print("Rollno:",self.rollno)
#         print("subjects with marks:")
#         print("HINDI:",self.hindi)
#         print("ENGLISH:",self.english)
#         print("SCIENCE:",self.science)
#         print("MATHS:",self.math)
#         print("GRADE:",val.grade())
     

# studentName=input("Enter name:")
# rollno=float(input("Enter Rollno.:"))
# eng=float(input("English marks:"))
# hin=float(input("Hindi amrks:"))
# math=float(input("Math marks:"))
# sci=float(input("Science marks:"))

# val=report_card(studentName,rollno,eng,sci,math,hin)

# val.per()
# val.grade()
# val.display_result()


####Create a class to display a message:
# class Message():

#     def displaye(self):
#        print("welcome to python!")

# msg=Message()
# msg.displaye()

####Class with constructor:
'Create a class Person with name and age, and print them using a method:'
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# msg=Person("kanika,23")
# msg.display()
'2'
# class Circle():
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return (22/7)*self.radius*self.radius
    
# pie=Circle(7)
# print("area of circle:",pie.area())

