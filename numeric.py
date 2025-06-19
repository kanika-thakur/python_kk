print("hello Dear")

#for adding spaces or break 
space="         "
print(space)

#heading
print("REPORT CARD")
print(space)

#subjects with marks 
print("MATHS")
maths=88
print(maths)
print(space)


print("ENGLISH")
eng=78
print(eng)
print(space)



print("SCIENCE")
sce=98
print(sce)
print(space)



print("SANSKRIT")
skt=98
print(skt)
print(space)



print("HINDI")
hin=98
print(hin)
print(space)


#calculate the sum of total numbers 
sum=maths+sce+eng+hin+skt
print("TOTAL")
print(sum)
print(space)


#calculate the percentage of all subjects
per=sum/500 *100
print(" PERCENTAGE")
print(per)
print(space)


#for the adding ,subtract,divide, multiplicat  the values using eval 
num1= eval(input("enter the first no."))
num2= eval(input("enter the secound no."))
res= num1+num2
print("the sum is "+str(res))
print(space)

subtract= num1-num2
print("the value is "+str(res))
print(space)


divide= num1/num2
print("the divide is "+str(res))
print(space)


multi= num1*num2
print("the multiplication is "+str(res))
print(space)


#try to make a marksheet 
print("KANIKA THAKUR")

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


#simple interest 
principle=eval(input("priciple is:"))
rate=eval(input("rate is:"))
time=eval(input("time is:"))


SI=(principle*rate*time)/100
print("simple interest is",str(SI))

#areas of rectangle 
l=eval(input("length1 is: "))
w=eval(input("width is: "))

rec=l*w
print("The area of rectangle is:"+str(rec))

#area of square 
l1= eval(input("length is :"))
l2=eval(input("length2 is :"))

sq=l1*l2
print("The area of square is:"+str(sq))



#road lights 
light=input("light color:")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken ")


#grades of students 
marks=input("enter marks:")
if(marks>=25):
 print("pass")
elif(marks<=25):
 print("fail")
else:
 print("none")

 





