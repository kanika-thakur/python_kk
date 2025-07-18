print("CALCULATOR:")
choice="Y"
while(choice=="Y") or (choice=="y"):
    num1=float(input("ENTER THE FIRST NUMBER:"))
    num2=float(input("ENTER THE SECOUND NUMBER:"))
    operator=str(input("ENTER THE OPERATOR DO U WANT TO PERFORM:"))
    if(operator=="*"):
        print("RESULT",num1*num2)
    elif(operator=="-"):
        print("RESULT",num1-num2)
    elif(operator=="/"):
        print("RESULT",num1/num2)
    elif(operator=="+"):
        print("RESULT",num1+num2)     
    elif(operator=="%"):
        print("RESULT",num1%num2)            
    else:
        print("error!")
    choice=str(input("Do you want to continue then type Y OTHERWISE N:"))


if(choice=="Y"):
   print("continue")
else:
   print("THANKS.....")




