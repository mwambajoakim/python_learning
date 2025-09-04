#!/usr/bin/python3
"""A banking system that does all operations"""
import time
import random
import datetime


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

      Args:
           account_holder: Account owner.
           initial_balance: Amount in the account.
    """
    monthly_interest = 0.5 / 100

    def __init__(self, account_holder, initial_balance=100):
        """Initialize a Savings Account"""
        super().__init__(account_holder)
        self.initial_balance = initial_balance

    def withdraw(self, amount):
        """Withdraw an amount from Savings Account

           Args:
                amount: Amount of money to withdraw.

           Return:
                  True if transaction is valid.
                  False if transaction is invalid.
        """
        if (self.initial_balance - amount) < self.initial_balance:
            return False
        self.initial_balance -= amount
        return True

    def apply_monthly_interest(self):
        """Apply a monthly interest to balance in account"""
        monthl_interest = SavingsAccount.monthly_interest * self.initial_balance
        return self.initial_balance + monthly_interest

    def get_account_type(self):
        """Return the account type"""
        return f"Account Type: Savings Account"


# ----------------------------------------------
# Checking Account
# ----------------------------------------------
class CheckingAccount(Account):

    def __init__(self, account_holder, initial_balance=0):
        """Initialize a Checking Account"""
        super().__init__(account_holder, initial_balance)

    def withdraw(self, amount):
        """Withdraw an amount from Savings Account

           Args:
                amount: Amount of money to withdraw.

           Return:
                  True if transaction is valid.
                  False if transaction is invalid.
        """
        diff = self.initial_balance - amount
        if diff >= -500:
            if diff <= 0:
                self.initial_balance -= 2
            self.initial_balance -= amount
            return True
        return False

    def get_overdraft_available(self):
        """Return amount of overdraft available"""
        if self.initial_balance >= 0:
            return 500
        if self.initial_balance < 0:
            return 500 + self.initial_balance

    def get_account_type(self):
        """Return the account type"""
        return f"Account Type: Checking Account"

# ----------------------------------------------------------
# Business Account
# ----------------------------------------------------------


class BusinessAccount(CheckingAccount):

    def __init__(self, account_holder, business_name, initial_balance=0):
        """Initialize a Business Account"""
        super().__init__(account_holder, initial_balance)
        self.business_name = business_name

    def withdraw(self, amount):
        """Withdraw an amount from Savings Account

           Args:
                amount: Amount of money to withdraw.

           Return:
                  True if transaction is valid.
                  False if transaction is invalid.
        """
        diff = self.initial_balance - amount
        if diff >= -2000:
            if diff <= 0:
                self.initial_balance -= 5
            self.initial_balance -= amount
            return True
        return False

    def get_overdraft_available(self):
        """Return the amount of overdraft available"""
        if self.initial_balance >= 0:
            return 2000
        if self.initial_balance < 0:
            return 2000 + self.initial_balance

    def get_account_type(self):
        """Return the account type"""
        return f"Account Type: Business Account"

    def get_account_info(self):
        """Get the information of an account"""
        return (
            f"Account Holder - {self.account_holder}\n"
            f"Account Balance - {self.initial_balance}\n"
            f"Business Name - {self.business_name}"
        )


# ----------------------------------------------------------
# Card Base Class
# ----------------------------------------------------------


class Card:
    """Initialize a card

       Args:
            linked_account: Account the card is associated to.
            card_type: If card is active or not.

       Return:
              A list of transactions done for each card
    """
    def __init__(self, linked_account, card_type):
        self.linked_account = linked_account
        self.card_type = card_type
        self.card_number = f"{random.randint(10**15, 10**16 - 1)}"
        self.is_active = True
        self.transactions = []

    def make_purchase(self, amount, merchant):
        """Make a purchase through a merchant

           Args:
                amount: Amount for the purchase.
                merchant: Merchant to complete transaction.

           Return:
                  List of transactions made.
        """
        if not self.is_active:
            raise ValueError("The card is inactive")
        if amount <= 0:
            raise ValueError("The amount must be positive")

        self.linked_account.withdraw(amount)
        transaction = {
            "amount": amount,
            "merchant": merchant,
            "date": datetime.datetime.now()
            }
        self.transactions.append(transaction)

    def get_card_info(self):
        """Return card information"""
        return (
            f"Account - {self.linked_account}\n"
            f"Card Type - {self.card_type}"
            )


# ---------------------------------------------------------
# Debit Card
# ---------------------------------------------------------


class DebitCard(Card):
    def __init__(self, linked_account, card_type):
        """Initialize a Debit Card"""
        super().__init__(linked_account, card_type)
        self.is_active = True
        self.transactions = []

    def make_purchase(self, amount, merchant):
        """Make a purchase through a merchant

           Args:
                amount: Amount for the purchase.
                merchant: Merchant to complete transaction.

           Return:
                  List of transactions made.
        """
        if not self.is_active:
            raise ValueError("The card is inactive")
        if amount <= 0:
            raise ValueError("The amount must be positive")
        if amount <= 1000:
            self.linked_account.withdraw(amount)
            transaction = {
                "amount": amount,
                "merchant": merchant,
                "date": datetime.datetime.now()
            }
            self.transactions.append(transaction)

# ----------------------------------------------------------------
# Credit Card
# ----------------------------------------------------------------


class CreditCard(Card):

    credit_limit = 5000

    def __init__(self, linked_account, card_type):
        """Initialize a Credit Card"""
        super().__init__(linked_account, card_type)
        self.is_active = True
        self.transactions = []

    def make_purchase(self, amount, merchant):
        """Make a purchase through a merchant

           Args:
                amount: Amount for the purchase.
                merchant: Merchant to complete transaction.

           Return:
                  List of transactions made.
        """
        if not self.is_active:
            raise ValueError("The card is inactive")
        if amount <= 0:
            raise ValueError("The amount must be positive")
        if amount < CreditCard.credit_limit:
            self.linked_account.withdraw(amount)
            transaction = {
                "amount": amount,
                "merchant": merchant,
                "date": datetime.datetime.now()
            }
            self.transactions.append(transaction)

# ----------------------------------------------------
# Account Management Functions
# ----------------------------------------------------
def create_account(account_type, holder_name, initial_deposit=0):
    """Factory function to create different account types"""
    accounts = {
        "savings": SavingsAccount,
        "checking": CheckingAccount,
        "business": BusinessAccount
        }
    account = accounts.get(account_type.lower())
    if account is None:
        raise ValueError("Enter a valid account type")
    return account(holder_name, initial_deposit)

def transfer_funds(from_account, to_account, amount):
    """Transfer money between accounts"""
    # Your implementation here
    pass

def generate_account_statement(account, start_date=None, end_date=None):
    """Generate formatted account statement"""
    # Your implementation here
    pass

def find_accounts_by_holder(accounts_list, holder_name):
    """Find all accounts belonging to a specific holder"""
    # Your implementation here
    pass
