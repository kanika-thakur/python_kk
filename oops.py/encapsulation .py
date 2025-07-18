'Create a class BankAccount with a private attribute __balance.'
' Add methods deposit(), withdraw(), and get_balance().'
' Prevent withdrawal if the amount is more than the balance.'
# class BankAccount():
#     def __init__(self,balance):
#         self.__balance=balance

#     def deposit(self,amount):
#         if(amount>0):
#          self.__balance+=amount
#         else:
#             print("error")

#     def withdraw(self,amount):
#         if(0<amount<=self.__balance):
#             self.__balance-=amount
#         else:
#             print("sorry ! insufficient money..")
    
#     def get_balance(self):
#         return self.__balance
    
# val = BankAccount(10000)
# print(val.deposit(500))
# print(val.withdraw(300))
# print("Balance:", val.get_balance())

# 'Create a class Employee with a private attribute __salary. '
# 'Create a getter and setter method for __salary.'
# ' Set validation to not allow negative salary.'
# class Employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
    
#     def`67`

'Create a class Student with private attributes __name and __rollno.'
'Add getter and setter methods for both.'
'Prevent setting empty name and negative roll number.'
class Student():
    def __init__(self,name,rollno):
        self.__name=name
        self.__rollno=rollno

    
    def get_method(self):
        return self.__name
        

    def set_method(self,new_name):
        if(new_name==" "):
            self.name=new_name
        else:
            print("invalid syntax")

    def set_method(self,new_rollno):
        if new_rollno<0:
            self.rollno= new_rollno
        else:
            print("invalid")

val=Student("kanika",34)
print("name:",val.set_rollno())
print("rollno:",val.get_method())

