'''
Created on Nov 28, 2022

@author: mj265496
'''
import atmWithdraw
import atmDeposit
import atmBalanceInquiry
import atmQuit

def opening():
    f = open("projectBalance.txt")
    balance = int(f.read())
    f.close()
    
    
    def start(b):
        balance = (b)
        x = 0
        while x < 1:
            #The x variable is used to let the user make multiple actions until they choose quit we'er its increased to 1
            #The y variable allows the user to re-input an amount or cancel a transaction if the remaining balance is less than $100
            y = False
            userInput = input("Please select an option (Deposit)(Withdraw)(Check Balance)(Quit):\n")
            userInput = userInput.lower()
    #Code checks if the user wants to deposit
            if userInput == "deposit":
                while y == False:
                    amount = int(input("Enter amount to deposit:"))
                    #Checking to make sure user input is not negative or zero, loops until user inputs a number greater than 0
                    if amount > 0:
                        balance = atmDeposit.deposit(balance, amount)
                        y = True
                    elif amount <= 0:
                        print("Deposit amount must be more than 0")
    #This code check if the user wants to withdraw                     
            elif userInput == "withdraw":
                while y == False:
                    amount = int(input("Enter amount to withdraw:"))
                    #Checking to make sure user input is not negative or zero, loops until user inputs a number greater than 0
                    if (amount > balance):
                        print("Insufficient Funds")
                    #Checks to make sure new balance wont be below $100 if so the code warns the user and then confirms that they still want to make the transaction
                    elif (balance - amount) < 100:
                        print("WARNING new balance will result in funds less than $100")
                        a = str(input("Do you wish to continue?(yes)(no):"))
                        a.lower()
                        if (a == "yes"):
                            balance = atmWithdraw.withdraw(balance, amount)
                            y = True
                        else:
                            print("Transaction Canceled")
    #The code checks the users balance if they inputed check balance                                        
                    elif amount > 0:
                        balance = atmWithdraw.withdraw(balance, amount)
                        y = True
    #This code will run if the users input is negative
                    elif amount <= 0:
                        print("Withdraw amount cannot be a negative number and must be more than 0")
    
    #Code will check the users balance
            elif userInput == "check balance":
                atmBalanceInquiry.Balance(balance)
    #Code will prince balance as well as exit message before ending the code
            elif userInput == "quit":
                atmQuit.Quit(balance)
                x = x + 1
    start(balance)
opening()