"craete a class bank account with a private attribute balance add method to deposit and withdraw money:"
class BankAccount():
    def __init__(self,accountname,balance):
        self.__accname=accountname
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        if(self.__balance<amount):
            self.__balance-=amount
        else:
            print("insufficient money!")

val=BankAccount("kanika",1000)
val.deposit(500)
val.withdraw(200)
       
     
    
