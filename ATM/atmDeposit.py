'''
Created on Nov 28, 2022

@author: mj265496
'''
import atmBalanceInquiry
def deposit(balance, amount):
    new = atmBalanceInquiry.calculateNewBalance(balance, amount)
    return(new)
