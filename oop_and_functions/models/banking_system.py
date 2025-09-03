#!/usr/bin/python3
"""A banking system that does all operations"""
import time


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
        print(f"{amount}")

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
# -----------------------------------
# Standalone functions
# -----------------------------------


def validate_amount(amount):
    """Validate if amount is positive and reasonable (less than 1 million)

       Args:
            amount: The amount of money to validate.

       Return:
              The amount of money after validation.
    """
    if amount < 0 or amount > 1000000:
        raise ValueError("Amount must be a positive number and reasonable")
    return amount


def calculate_interest(principal, rate, time_years):
    """Calculate simple interest: P * R * T / 100

       Args:
            amount: The principal amount of money.

       Return:
              The simple interest on the principal amount.
    """
    return (principal * rate) * time_years / 100


def format_currency(amount):
    """Format amount as currency (e.g., 1234.56 -> '$1,234.56')

       Args:
            amount: The money as an unformatted string

       Return:
              The formatted string of the amount.
    """
    return f"${amount:,}"


def generate_transaction_id():
    """Generate unique transaction ID using timestamp

       Return:
              The date and time of transaction
    """
    return time.ctime()


# ------------------------------------------
# Inheritance
# -----------------------------------------
class SavingsAccount(Account):
    """Creates a savings account.
       It inherits from the class Account.
    """
    monthly_interest = 0.5 / 100

    def __init__(self, account_holder, initial_balance=100):
        super().__init__(account_holder)
        self.initial_balance = initial_balance

    def withdraw(self, amount):
        if (self.initial_balance - amount) < self.initial_balance:
            return False
        self.initial_balance -= amount
        return True

    def apply_monthly_interest(self):
        intr = SavingsAccount.monthly_interest * self.initial_balance
        return self.initial_balance + intr

    def get_account_type(self):
        return f"Account Type: Savings Account"
