# I used Thonny to write this code, thats why I put the CheckingAccount class and the driver here in the same file
class CheckingAccount:
    #create a constructore for the class

    def __init__(self,name,address,accountNumber,balance):
        
        #private local variables
        self.__name = name;
        self.__address = address
        self.__accountNumber = accountNumber
        self.__balance = balance
        
    # define methods to access the private instance variables outside of the class
    def retrunName(self):
        return self.__name
    def returnAddress(self):
        return self.__address
    def returnAccountNumber(self):
        return self.__accountNumber
    def returnBalance(self):
        return self.__balance


    #a method to deposite money
    def depositeToAccount(self,deposite):
        self.__balance = self.__balance + deposite

    #a methof to withdraw money
    def withdrawalFromAccount(self,withdrawal):
        self.__balance = self.__balance - withdrawal
    
    #overRide the string Method
    def __str__(self):
        
        return "Account Holder Name: {}\nAddress: {}\nAccount Number: {}\nAccount Balance: ${}".format(self.__name,self.__address,self.__accountNumber,self.__balance )
        
       

       
##diver main Method
def main():
    
    #create a new instance of the CheckingAccount Type
    newAccount= CheckingAccount("Alula Mekonen","500 blick drive", 21772009, 2000)
    
    print("Account detail Before Deposite\n")
    print(newAccount)
    print("-----------------------------------------------------------------------\n")
    
    #amount to be deposited and withrew
    depositeAmount = 3000
    withdrawalAmount = 300
    
    #deposite money
    newAccount.depositeToAccount(depositeAmount)
    
    #display the account detail
    print("Account detail After Deposite\n")
    print(newAccount)
    print("-----------------------------------------------------------------------\n")
    
    #check if the balance is enough and withdrawal money
    if newAccount.returnBalance() < withdrawalAmount:
        print("you dont have enough Balance\n")
        print("-----------------------------------------------------------------------\n")
    else:
        newAccount.withdrawalFromAccount(withdrawalAmount)
        
    #display the account detail
    print("Account detail After withdrawal\n")
    print(newAccount)
    print("-----------------------------------------------------------------------\n")
       
    
#call the main method            
main()
    




