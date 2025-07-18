# class Employee():
#     empcount=0
#     def __init__(self,name,dept):
#         self.name=name
#         self.dept=dept
#         pass
#         Employee.empcount+=1
#         print(self.name)
#         print(self.dept)
#         print(Employee.empcount)

# emp=Employee('kanika','training')
# emp2=Employee("a","b")

'Create a class Car with a class attribute wheels = 4. '
'Create two car objects and print number of wheels using each object.'
# class Car():
#     wheels=4
#     def __init__(self,brand):
#         self.car=brand

    

# val1=Car('maruti')
# val2=Car('scorpio')

# print("car one is:",val1.wheels)
# print("car two is:",val2.wheels)

# print("all cars have:",Car.wheels)


' Define a class Laptop with a class attribute brand = "Dell". '
'Create two objects and print the brand using both the class and objects'
# class Laptop():
#     brand="Dell"
#     def __init__(self,brand):
#         self.brand=brand
#         pass

# val1=Laptop('lenovo')
# val2=Laptop("hp")

# print(val1.brand)
# print(val2.brand)

# print(Laptop.brand)

'Create a class Mobile with class attribute category = "Smartphone".'
'Change the class attribute using the class name. Print it using an object.'
# class Mobile():
#     category="Smartphone"
#     def __init__(self,brand):
#         self.name=brand

# obj=Mobile('vivo')
# obj2=Mobile("samsung")

# print("before changing:")
# print("obj category: ",obj.category)
# print("obj2 category:",obj2.category)

# print("all mobile categories:",Mobile.category)

# Mobile.category="android-phone"
# print("after changing :")
# print("obj category:",obj.category)
# print("obj2 category:",obj2.category)

# print("all categories of mobile:",Mobile.category)

'Define a class Student with class attribute school_name = "ABC High School".'
'Use the constructor to accept name and roll number. Print all three values for two objects.'
# class Student():
#     school_name="ABC High School"
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

# val1=Student("kanika",34)
# val2=Student("komal",23)

# print(val1.school_name)
# print(val2.school_name)

# print(Student.school_name)

# print(val1.name,val1.rollno,val1.school_name)
# print(val2.name,val2.rollno,val2.school_name)

'Create a class Book with class attribute library = "City Library".'
'Add instance attributes for title and author.'
'Change the class attribute using one object. What happens?'
# class Book():
#     library="city library"
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

# obj=Book("rich dad and poor dad ","robert")
# obj.library="centeral librry"
# print(obj.library)


' Define a class Employee with class attribute company = "Google".'
'Also, define a method change_company() that updates the class attribute.'
# class Employee():
#     company="google"
    
#     def change_company():
#         print("cimpany changed")

# print("before changing:",Employee.company)

# Employee.change_company="browser"

# print("after changing:",Employee.change_company)

' Create a class Counter with a class attribute count = 0'
'In the __init__() method, increment count each time an object is created'
'Print total objects after creating 5 objects.' 
# class Counter():
#     count=0
#     def __init__(self,count):
#         self.count=count
#         Counter.count+=1

# obj1=Counter(1)
# obj2=Counter(2)
# obj3=Counter(3)
# obj4=Counter(4)
# obj5=Counter(5)


# print("total created objects:",Counter.count)


'built in class attributes:'
# class Employee():
#     def __init__(self,name="kanika",age=24):
#         self.name=name
#         self.age=age

#     def show(self):
#         print("name:",self.name," , age:",self.age)
7
# print("employee.__doc__:", Employee.__doc__)
# print("employee.module:", Employee.__module__)
# print("employee.name:", Employee.__name__)
# print("employee.bases:", Employee.__bases__)
# print("employee.dict:", Employee.__dict__)





    

             
        








