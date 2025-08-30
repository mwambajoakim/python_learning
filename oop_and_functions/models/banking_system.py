#!/usr/bin/python3
"""A banking system that does all operations"""


class Account:
    # Class variable for generating unique account numbers
    _account_counter = 1000
    
    def __init__(self, account_holder, initial_balance=0):
        """Define the account holder and initial balance in account"""
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        # Your implementation here
        pass
    
    def withdraw(self, amount):
        # Your implementation here  
        pass
    
    def get_balance(self):
        # Your implementation here
        pass
    
    def get_account_info(self):
        # Your implementation here
        pass
