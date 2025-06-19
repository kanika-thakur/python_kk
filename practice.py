#addmission form
#full name
print("ADDMISSION FORM")
name=input("FIRST NAME:")
name2=input("SECOUND NAME:")

#age
age=int(input("AGE:"))

#date of birth
dob=input("DATE OF BIRTH:")



#10th marks
matric= int(input("10TH PERCENTAGE:"))

#+2 marks
base=int(input("+2 PERCENTAGE:"))



print("  ")
print("FULL NAME:", (name)+"  "+(name2))
print("AGE:",age)
print("DOB:",dob)
print("10TH PERCENTAGE:",matric)
print("+2 PERCENTAGE :",base)



if(age>30):
    print("you are eligible.")
elif(age<30):
    print(" sorry...you are not eligible!")
elif(matric>50):
    print("good,you are eligible")
elif("matric<50"):
    print(" sorry...you are not eligible!")
elif(base>50):
    print("good,you are eligible")
else:
     print(" sorry...you are not eligible!")


    




"""if(matric>50):
    print("good,you are eligible")
else:
    print(" sorry...you are not eligible!")


if(base>50):
    print("good,you are eligible")
else:
    print(" sorry...you are not eligible!")"""


    

