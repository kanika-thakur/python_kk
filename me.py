marks=input("enter marks:")
if(marks>=90):
    print("topper")
elif(marks>=80)and(marks<90):
    print("medium")
elif(marks>=70) and (marks<80):
    print("low level")
else:
    print("fail")
    

#airthmetic operator
a=13
b=45
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#relational operator/ comparison operator
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)

#assignment operatorrint
num=10
num/=5

#logical operator 
a=50
b=57
val1 = True 
val2 = False
print(" AND operator:", val1 and val2)
print("OR perator:",(a == b) or (a > b))

#type conversion 
#tytpe casting
a= "kanika" 
b=str(a)
print(a+b)
print(type(a))

#input in python 
name1=input("enter your first name:")
name2=input("enter your last name:")
print((name1) + (name2))

name=input("enter name:")
age=int(input("enter age:"))
marks= float(input("enter marks:"))

print("welcome",name)
print("age =",age)
print("marks =",marks)

name=input("FIRST NAME:")
print(name)
print(len(name))

str="hi,$Iam the $ symbol $9.99"
print(str.count("$"))




