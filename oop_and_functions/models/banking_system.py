#!/usr/bin/python3
"""A banking system that does all operations"""
from datetime import datetime


class Account:
    # Class variable for generating unique account numbers
    _account_counter = 1000
    
    def __init__(self, account_holder, initial_balance=0):
        """Define the account holder and initial balance in account"""
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        """Records the  deposit of an amount of money"""
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number")
        self.initial_balance += amount
    
    def withdraw(self, amount):
        """Records the withdrawal of an amount of money"""
        if self.initial_balance > amount:
            self.initial_balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Returns the balance in the account"""
        return self.initial_balance
    
    def get_account_info(self):
        """Get the information of an account"""
        return f"Account Holder - {self.account_holder} Account Balance - {self.initial_balance}"
