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
        Account._account_counter += 1

    def deposit(self, amount):
        """Records the  deposit of an amount of money"""
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
        return f"""
        Account Holder - {self.account_holder}
        Account Balance - {self.initial_balance}
        """
#-----------------------------------
# Stand alone functions
#-----------------------------------

def validate_amount(amount):
    """Validate if amount is positive and reasonable (less than 1 million)"""
    if amount < 0 or amount > 1000000:
        raise ValueError("Amount must be a positive number and reasonable")
    return amount

def calculate_interest(principal, rate, time_years):
    """Calculate simple interest: P * R * T / 100"""
    return (principal * rate) * time_years / 100

def format_currency(amount):
    """Format amount as currency (e.g., 1234.56 -> '$1,234.56')"""
    return f"${amount:,}"
    

def generate_transaction_id():
    """Generate unique transaction ID using timestamp"""
    # Your implementation here
    pass
