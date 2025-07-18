'SINGLE INHERITENCE:'
# class Namefirst():
#     def __init__(self,firstname,lastname):
#         self.firstname=firstname
#         self.lastname=lastname

#     def get_full_name(self):
#         print(self.firstname+self.lastname)

# class NameLast(Namefirst):
#     def __init__(self, firstname, lastname,age):
#         super().__init__(firstname, lastname)
#         self.age=age
    
#     def GetAge(self):
#         print(self.age)
    
# mn=NameLast('kanika','thakur',20)
# mn.get_full_name()
# mn.GetAge()

'create a Person class (Parent) and a Student class (Child) that inherits from it:'
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get(self):
#         print("name:",self.name)
#         print("age:",self.age)

# me=

# 'add two numbers in base class and add three numbers in the derive class:'
# class Numbers():
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def add(self):
#         return (self.num1+self.num2)
        


# class Number2(Numbers):
#     def __init__(self, num1, num2,num3):
#         super().__init__(num1, num2)
#         self.num3=num3

#     def add2(self):
        
#         return self.num1+self.num2+self.num3



# sum=Number2(23,34,56)
# print("sum of two numbers:",sum.add())
# print("sum of two numbers:",sum.add2())


# 'calculate area of square in abse class and area of rectangle in derive class:'
# class Square():
#     def __init__(self,length):
#         self.length=length
    
#     def area(self):
#         return self.length*self.length

# class Rectangle(Square):
#         def __init__(self, length,width):
#             super().__init__(length)
#             self.width=width
        
#         def areaR(self):
#             return self.length*self.width
        
# result=Rectangle(2,5)
# print("Area of Square:",result.area())
# print("Area of Rectangle:",result.areaR())

# 'craete a person as a base class and student as a derived class, student has id and name as parameter, and student has course and grade calll th detil of the students:'
# class Person():
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name

# class Student(Person):
#     def __init__(self, id, name,course,grade):
#         super().__init__(id, name)
#         self.course=course
#         self.grade=grade
    
#     def details(self):
#         print("id is:",self.id)
#         print("name is:",self.name)
#         print("course is:",self.course)
#         print("grade is:",self.grade)

# val=Student("kanika12","kanika thakur","BCA","A+")
# val.details()

# '2=>'
# class Animal():
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         return " animal sound"

# class Dog(Animal):
       
#     def speak(self):
#          return f"{self.name} says woof!"

# nm=Dog("buddy")
# print(nm.speak())

# 'design a class product with attributes name,price. create a class discountedproduct that inherits from product and adds a method to calculate price after discount:'
# class Product():
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class DiscountedProduct(Product):
#     def __init__(self, name, price,discount_per):
#         super().__init__(name, price)
#         self.discount_per=discount_per

#     def calculate_price(self):
#         return(self.discount_per/100)*self.price
    

# price=int(input("enter price:₹",))
# discount_per=int(input("Discount:%",))

# val=DiscountedProduct("wire",price,discount_per)
# print("price after discount:",val.calculate_price())

'Create a class Animal with a method speak() and a child class Dog that inherits it:'
# class Animal():
#     def speak (self):
#      print("animal speaks")

# class Dog(Animal):
#     pass
 
# val=Animal()
# print(val.speak())

'Create a class Vehicle with brand and year. Inherit it in a class Car and print both values:'
# class Vehicle():
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
    
# class Car(Vehicle):
#         pass

# p1=Vehicle("maruti",1990)
# print(p1.brand)
# print(p1.year)

' Create a parent class with a method message(). Call it from a child class along with its own method:'
# class Parent():
#     def __init__(self):
#         pass
#     def message(self):
#        print("hllo")
#        pass
        
# class Child(Parent):
#     def message2(self):
#         print("hello from child")

# c1=Parent()
# c1.message()

'Modify the child class to use super() to call the parent class method:'
# class StudentIntro():
#     def __init__(self,name,course,):
#         self.name=name
#         self.course=course
    
#     def show(self):
#         print("studentintro:",self.name,self.course)
    
# class course(StudentIntro):
#     def __init__(self, name, course,courseyear,coursefees):
#         super().__init__(name, course)
#         self.courseyear=courseyear
#         self.coursefees=coursefees

#     def display(self):
#         print("all details:",self.name,self.course,self.coursefees,self.courseyear)


# a=StudentIntro("kanika","BCA")
# a=course()
# a.show()
# a.dispaly

'addition and subtraction using inheritence:'
# class Add():
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def calculate(self):
#         return self.num1+self.num2

# class Subtract(Add):
#         def __init__(self, num1, num2):
#             super().__init__(num1, num2)
        
#         def calculate(self):
#             return self.num1-self.num2
        
# val=Subtract(50,10)
# val2=Add(34,56)
# print("subtract:",val.calculate())
# print("add:",val2.calculate())


'multilevel inheritence:'
# class Animal():
#      def __init__(self,name):
#           self.name=name

#      def speak(self):
#           print("sounds")
#           print("Animal name:",self.name)
# class Dog(Animal):
#           def __init__(self, name,age):
#                super().__init__(name)
#                self.age=age
#           def speak(self):
#                print("dog barks")
#                print("Animal name:",self.name)
#                print("Dog age :",self.age)

# class cat(Dog):
#         def __init__(self, name, age,breed):
#              super().__init__(name, age)
#              self.breed=breed
#         def speak(self):
#              print("meow")
#              print("cat name:",self.name)
#              print("cat age:",self.age)
#              print("cat breed:",self.breed)

# val=cat("bunny",5,"breed")
# val1=Animal('dog')
# val2=Dog("rocky",2)
# val.speak()
# val1.speak()
# val2.speak()

'2 Create a multilevel inheritance for Person → Employee → Manager. Print all attributes:'
# class Person():
#     def __init__(self,name,age,hieght):
#         self.name=name
#         self.age=age
#         self.hiegth=hieght


# class Employee(Person):
#     def __init__(self, name, age, hieght,empDep,salary):
#         super().__init__(name, age, hieght)
#         self.empdep=empDep
#         self.salary=salary

    
        

# class Manager(Employee):
#     def __init__(self, name, age, hieght, empDep, salary,department):
#         super().__init__(name, age, hieght, empDep, salary)
#         self.dep=department

#     def show(self):
#        print("name:",self.name)
#        print("age:",self.age)
#        print("salary",self.salary)
#        print("department:",self.empdep)
#        print("department:",self.dep)
    
# val=Manager("kanika",21,'5ft','queue',20000,'human-resource')
# print(val.show())

' Animal → Mammal → Dog. Print details using method overriding:'
# class Animal():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Mammal(Animal):
#         def __init__(self, name, age,):
#              super().__init__(name, age)
      
# class Dog(Mammal):
#      def __init__(self, name, age,breed):
#           super().__init__(name, age)
#           self.breed=breed
        
#      def show(self):
#         print(
#             f" name:{self.name}\n"
#             f" age: {self.age} \n"
#             f" breed: {self.breed}\n"
#         )
# val=Dog("rocky",5,"huskey")
# val.show()

'Create classes: Shape → Rectangle → Box. Calculate area and volume:'
# class Shape():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

# class Rectangle(Shape):
#        def area (self):
#            return self.length*self.width
    
# class Box(Shape):
#     def __init__(self, length, width,hieght):
#         super().__init__(length, width)
#         self.hieght=hieght

#     def area2(self):
#          return 2*(self.length*self.width+self.width*self.hieght+self.hieght*self.length)
     
#     def vol(self):
#          return self.length*self.width*self.hieght
    
# val=Box(12,23,4,)
# val2=Rectangle(23,34)
# print("area of box:",val.area2())
# print("volume of box:",val.vol())
# print("volume of rectangle:",val.vol())
# print("area of rectangle:",val2.area())

'Vehicle → Car → ElectricCar. Show method chaining with super():'
# class Vehicle():
#    def vehicle(self):
#       print("vehicle")

# class Car(Vehicle):
#    def car(self):
#       super().vehicle()
#       print("car")

# class ElectricCar(Car):
#    def electriccar(self):
#       super().car()
#       print("electriccar")

# a=ElectricCar()
# a.electriccar()
          
'Create a Person class with name and age, and an Employee class that inherits from Person.'
' Add a method display() in Employee that prints name and age.'
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Employee(Person):
#         def __init__(self, name, age,):
#              super().__init__(name, age)
       
#         def display(self):
#              print("name:",self.name)
#              print("age:",self.age)

# val=Employee("kanika",20)
# val.display()

'Create a Vehicle class with a method start(), and a Car class that inherits it and adds a method drive().'
' Call both methods from a Car object.'
# class Vehicle():
#     def start(self):
#         print("set")

# class car(Vehicle):
#     def drive(self):
#         print("set2")

# obj=car()
# print(obj.start())
# print(obj.drive())


'4️⃣ Create a Student class with an __init__() method and a display() method.'
' Inherit CollegeStudent and add college_name.'
' Use super() to call the parent class constructor.'
# class Student():
#     def __init__(self,collageStudent,studentName):
#         self.student=collageStudent
#         self.name=studentName
    

# class Student2(Student):
#         def __init__(self, collageStudent, studentName):
#              super().__init__(collageStudent, studentName)
            
#         def display(self):
#          print("student of college:",self.student)
#          print("name of student:",self.name)
#         pass
# val=Student2('gpgc','kanika')
# val.display()


'5️⃣ Write a program where a Rectangle class has length and width, and a Box class inherits it and adds height.'
'Add methods for area() and volume().'
# class Rectangle():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
    
#     def area1(self):
#         return self.length*self.width
    
# class Box(Rectangle):
#         def __init__(self, length, width,hiegth):
#              super().__init__(length, width)
#              self.hiegth=hiegth
        
#         def area(self):
#           return self.length*self.width+self.width*self.hiegth+self.hiegth*self.length
        
#         def volume(self):
#             return self.length*self.width*self.hiegth

# val=Box(2,3,6)
# print("area of rectangle:",val.area1())
# print("area of box:",val.area())
# print("volume of box:",val.volume())

'6️⃣ Create three classes: GrandParent, Parent, and Child using multilevel inheritance.'
' Each should have a show() method. Call all using a Child object.'
# class GrandParent():
#     def __init__(self):
#         pass
#     def show(self):
#         print("jskf")
# class Parent(GrandParent):
#     def __init__(self):
#         super().__init__()

#     def show(self):
#         print("jbsdkj")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()

#     def show(self):
#         print("hjgug")

# object=GrandParent()
# object.show()


'9️⃣ Create a base class Device with method power_on(). Inherit Mobile and Laptop. Override power_on() differently in each class.'
# class Device():
#     def __init__(self,mobile,laptop):
#         self.name=mobile
#         self.develop=laptop


#     def power_on(self):
#         print("Device")

# class NewDevice(Device):
#         def __init__(self, mobile, laptop):
#              super().__init__(mobile, laptop)

#         def power_on(self):
#              print("new devices")

# obj=Device('mobile','laptop')
# obj2=NewDevice('android','lenovo')
# obj.power_on()
# obj2.power_on()



    




'hierarcical inheritence'
# class Animal():
#      def __init__(self,name):
#           self.name=name

#      def speak(self):
#           print("sounds")
#           print("Animal name:",self.name)
# class Dog(Animal):
#           def __init__(self, name,age):
#                super().__init__(name)
#                self.age=age
#           def speak(self):
#                print("dog barks")
#                print("Animal name:",self.name)
#                print("Dog age :",self.age)

# class cat(Animal):
#         def __init__(self, name,breed):
#              super().__init__(name)
#              self.breed=breed
#         def speak(self):
#              print("meow")
#              print("cat name:",self.name)
#              print("cat breed:",self.breed)

# val=cat("bunny","breed")
# val1=Animal('dog')
# val2=Dog("rocky",2)
# val.speak()
# val1.speak()
# val2.speak()

# 'hierarchical inheritence:'
# class A():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def show(self):
#         return self.a+self.b
    
# class B(A):
#         def __init__(self, a, b,c):
#              super().__init__(a, b)
#              self.c=c

#         def add(self):
#              return self.a+self.b+self.c

# class C(A):
#         def __init__(self, a, b,d):
#              super().__init__(a, b)
#              self.d=d

#         def sum(self):
#              return self.a+self.b+self.d
        

# val=B(12,23,4)
# val2=C(2,3,4)
# print("sum:",val.add())
# print("sum:",val2.sum())
        


# 'multiple inheritence:'
# class A():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def show(self):
#         return self.a+self.b
    
# class B():
#         def __init__(self,c,d):
#             self.c=c
#             self.d=d


#         def add(self):
#              return self.c+self.d
        
# class C(A,B):
#      def __init__(self, a, b,c,d):
#           A.__init__(self,a,b)
#           B.__init__(self,c,d)
        
#      def display(self):
#           return self.d
     
# value=C(2,3,4,5)
# print("vale:",value.display())

'Create class Person with method details(), and class Employee with method job().'
' Inherit both into class Manager. Print name and job title'
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def details(self):
#         print("name:",self.name)
#         print("age:",self.age)

# class Employee():
#         def __init__(self,jobname,salary):
#              self.jobname=jobname
#              self.salary=salary

#         def job(self):
#              print("jobname:",self.jobname)
#              print("salary:",self.salary)
# class Manager(Person,Employee):
#         def __init__(self, name, age,jobname,salary):
#             Person.__init__(self,name, age)
#             Employee.__init__(self,jobname,salary)
        
#         def show (self):
#              return
        

# val=Manager("kanika",20,"training",20000)
# print(val.details())
# print(val.job())
        
'Create two classes Rectangle (length, width) and Paint (color).'
' In class ColoredRectangle, inherit both and display area and color'
# class Rectangle():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
    
    
# class Paint():
#         def __init__(self,color):
#              self.color=color

# class ColoredRectangle(Rectangle,Paint):
#             def __init__(self, length, width,color):
#                 Rectangle.__init__(self,length, width)
#                 Paint.__init__(self,color)

#             def area(self):
#              print("area:", self.length*self.width)
            
#             def show(self):
#              print("color:",self.color)
            
# val=ColoredRectangle(2,4,'red')
# val.area()
# val.show()

'Class Person with name.'
' Class Employee(Person) and Student(Person). '
'Class Intern(Employee, Student) should show all details.'
# class Person():
#     def __init__(self,name,course,age):
#         self.name=name
#         self.course=course
#         self.age=age

# class Employee(Person):
#     def __init__(self, name, course, age,fees):
#         super().__init__(name, course, age)
#         self.fees=fees
    
# class Student(Person):
#     def __init__(self, name, course, age,gender):
#         super().__init__(name, course, age)
#         self.gender=gender

# class Intern(Employee,Student):
#     def __init__(self, name, course, age, fees,gender):
#        Employee.__init__(self,name, course, age, fees)
#        Student.__init__(self,name, course, age,gender)
    
#     def details(self):
#         print("name:",self.name)
#         print("course:",self.course)
#         print("fees:",self.fees)
#         print("gender:",self.gender)

# val=Intern("kanika","training",20,20000,"female")
# val.details()


'Class Animal has eat(), class Bird has fly(). Create class Bat using multiple inheritance. '
'Override both methods to show Bat-specific behavior.'
# class Animal():
#     def eat(self):
#         print("meal")

# class Bird():
#     def fly(self):
#         print("sky")

# class Bat(Bird,Animal):
#     def eat(self):
#         print("bat eats insights at night ")

#     def fly(self):
#         print("Bat flies using wings like birds")

# b=Bat()
# b.eat()
# b.fly()
   
'hierarchicle inheritence:'
'Class Vehicle has a method start().'
' Class Car and Bike inherit from it and define their own method drive() / ride().'
' Create objects and call all methods.'
# class Vehicle():
#     def start(self):
#         print("car start!!")

# class Car(Vehicle):
#     def drive(self):
#         print("drive slowly ")

# class Bike(Vehicle):
#     def ride(self):
#         print("ride")

# val=Car()
# val2=Bike()
# val1=Vehicle()
# val.drive()
# val2.ride()
# val1.start()

'Class Shape has method display().'
' Class Circle and Square inherit it and define their own area calculation. '
'Take input from the user.'
# class shape():
#     def __init__(self,r1):
#         self.r1=r1

# class circle(shape):
#     def __init__(self, r1):
#         super().__init__(r1)

#     def areaC(self):
#         return (22/7)*self.r1**2
    

# class Square(shape):
#     def __init__(self, r1):
#         super().__init__(r1)
#     def areaS(self):
#         return self.r1**2

# r1=int(input("enter the numebr:"))
# val=circle(r1)
# print("area of circle:",val.areaC())
# val=Square(r1)
# print("area of square:",val.areaS())


'Create class Person. Inherit it to Student and Teacher. '
'Add role-specific methods.'
' Print details for both student and teacher objects.'
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def display_info(self):
#          print("name:",self.name)
#          print("age:",self.age)

# class Student(Person):
#         def __init__(self, name, age,course):
#              super().__init__(name, age)
#              self.course=course

#         def display(self):
#              print("course:",self.course)

# class Teacher(Person):
#         def __init__(self, name, age,salary):
#               super().__init__(name, age)
#               self.salary=salary
        
#         def show(self):
#               print("salray:",self.salary)

# val=Student("aknika",21,"training")
# val.display()
# val=Teacher("kanika",21,20000)
# val.show()    







       
        
     



