#function=>
#defining a function
def greet():
    print("hello world!")

#calling a function
greet()

#define with parameters
def greet(name):
    print("hello",name)

#calling  with arguments
greet('kanika')


#function with return value=>
def add(a,b):
    return a+b
result= add(8,9)
print(result)

#default parameters=>
def greet(name="radha"):
    print("hello",name)

greet()
greet("shyam")


#keywords=>
def student_info(name,age):
    print("Name:", name)
    print("Age:",age)

student_info(name='kanika',age=13)

# *args=< used for multiple positional arguments:
def numbers(*numbers):
     return sum(numbers)
print(numbers(1,23,34,5,6,6))
numbers()


