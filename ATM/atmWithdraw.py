'''
Created on Nov 28, 2022

@author: mj265496
'''
import atmBalanceInquiry
def withdraw(balance, amount):
    amount = amount * -1
    new = atmBalanceInquiry.calculateNewBalance(balance, amount)
    return(new)    