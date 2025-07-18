#if-else statement 
a=2
b=5
if (b>a):
    print("b is greater than a")
    print()
else:
    print("b is not greater than a ")
    print()

#elif statment
a=44
b=23
if (a<b):
    print("b is greater than b ")
    print()
elif a==b:
  print("a and b are equal ")
  print()

#else statement
if (a<b):
    print("a is greater than b")
    print()
elif(a==b):
    print("a and b are equal")
else:
    print("a is greater than b ")
    print()


#shorthand if
if(a>b):print("a is greater than b ")    
print()


#short hand if else statement 
a=23
b=45
print("A") if (a<b) else print("B")
print()


#AND is used to combine conditional statements 
if (a <b) and (a<b) : 
    print ("both condtions are true !!")
    

#OR as same as AND
if a <b or a>b :
    print("both conditons are not true!!!")


#NOT is used to reverse the conditional statements
if not a>b :
    print("a is not greater than b")


#one line if statement with three conditions
print("A") if a<b else print("=") if a==b else print("B")


#one line if else statement 
print("RIGHT") if a<b else print("WRONG")


#nested if statements--- inside the if statement inside the if statements 
x=10
if x>10:
 print("above 10!")
 if x>20:
     print("above 20!")
else:
    print("not above 20!!")



#the pass statement
if b>a :
    print("PASS")
else :
    print("SORRY!! YOU ARE FAIL")


#python match statement
day=5
match day:
    case 1:
        print("SUNDAY")
    case 2:
        print("MONDAY")
    case 3:
        print("TUESDAY")
    case 4:
        print("WEDNESDAY")
    case 5:
        print("THURSDAY")
    case 6:
        print("FRIDAY")
    case 7:
        print("SATURDAY")
  


  #default value
day=4
match day :
  case 4:
    print("today is  SATURDAY")
  case 5:
     print("today is SUNDAY")
  case _:
     print("looking forward to the next weekend")


#combine values 
        





