'''
Created on Nov 28, 2022

@author: mj265496
'''
def Quit(balance):
    f = open("Jonesfile.txt", "w")
    newEntry = str(balance)
    f.write("Balance:$%s\n"%newEntry)
    f.write("Thank you for choosing our ATM")
    f.close()
    f = open("Jonesfile.txt")
    contents = f.read()
    print(contents)
    f.close()

