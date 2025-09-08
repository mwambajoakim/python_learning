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
        __class__._account_counter += 1
        self.transactions = []

    def deposit(self, amount):
        """Records the  deposit of an amount of money"""
        self.initial_balance += amount
        transaction = {
            "transaction_type": "deposit",
            "amount": amount,
            "date": datetime.datetime.now()
            }
        self.transactions.append(transaction)
        return amount

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
    earned_interest = 0.5 / 100

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
        initial_balance_difference = self.initial_balance - amount
        floor_balance_amount = 100
        if initial_balance_difference < floor_balance_amount:
            return False
        self.initial_balance -= amount
        transaction = {
            "transaction_type": "withdrawal",
            "amount": amount,
            "date": datetime.datetime.now()
            }
        self.transactions.append(transaction)
        return True

    def apply_monthly_interest(self):
        """Apply a monthly interest to balance in account"""
        balance = self.initial_balance
        monthly_interest = SavingsAccount.earned_interest * balance
        return balance + monthly_interest

    def get_account_type(self):
        """Return the account type"""
        return f"Account Type: Savings Account"


# ----------------------------------------------
# Checking Account
# ----------------------------------------------


class CheckingAccount(Account):

    overdraft_amount = 500

    def withdraw(self, amount):
        """Withdraw an amount from Savings Account

           Args:
                amount: Amount of money to withdraw.

           Return:
                  True if transaction is valid.
                  False if transaction is invalid.
        """
        balance_amount_difference = self.initial_balance - amount
        overdraft_deduction = 2
        if balance_amount_difference >= -CheckingAccount.overdraft_amount:
            if balance_amount_difference <= 0:
                self.initial_balance -= overdraft_deduction
            self.initial_balance -= amount
            transaction = {
                "transaction_type": "withdrawal",
                "amount": amount,
                "date": datetime.datetime.now()
            }
            self.transactions.append(transaction)
            return True
        return False

    def get_overdraft_available(self):
        """Return amount of overdraft available"""
        if self.initial_balance >= 0:
            return CheckingAccount.overdraft_amount
        if self.initial_balance < 0:
            return CheckingAccount.overdraft_amount + self.initial_balance

    def get_account_type(self):
        """Return the account type"""
        return f"Account Type: Checking Account"

# ----------------------------------------------------------
# Business Account
# ----------------------------------------------------------


class BusinessAccount(CheckingAccount):

    overdraft_amount = 2000

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
        balance_amount_difference = self.initial_balance - amount
        overdraft_deduction = 5
        if balance_amount_difference >= -BusinessAccount.overdraft_amount:
            if balance_amount_difference <= 0:
                self.initial_balance -= overdraft_deduction
            self.initial_balance -= amount
            transaction = {
                "transaction_type": "withdrawal",
                "amount": amount,
                "date": datetime.datetime.now()
            }
            self.transactions.append(transaction)
            return True
        return False

    def get_overdraft_available(self):
        """Return the amount of overdraft available"""
        if self.initial_balance >= 0:
            return BusinessAccount.overdraft_amount
        if self.initial_balance < 0:
            return BusinessAccount.overdraft_amount + self.initial_balance

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

    def make_purchase(self, amount, merchant):
        """Make a purchase through a merchant

           Args:
                amount: Amount for the purchase.
                merchant: Merchant to complete transaction.

           Return:
                  List of transactions made.
        """
        if amount <= 1000:
            if self.linked_account.withdraw(amount):
                transaction = {
                    "amount": amount,
                    "merchant": merchant,
                    "date": datetime.datetime.now()
                }
                self.transactions.append(transaction)
        else:
            raise ValueError("Exceeds daily spend")
# ----------------------------------------------------------------
# Credit Card
# ----------------------------------------------------------------


class CreditCard(Card):

    credit_limit = 5000

    def make_purchase(self, amount, merchant):
        """Make a purchase through a merchant

           Args:
                amount: Amount for the purchase.
                merchant: Merchant to complete transaction.

           Return:
                  List of transactions made.
        """
        if amount < CreditCard.credit_limit:
            if self.linked_account.withdraw(amount):
                transaction = {
                    "amount": amount,
                    "merchant": merchant,
                    "date": datetime.datetime.now()
                }
                self.transactions.append(transaction)
        else:
            raise ValueError("Exceeds credit limit")

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
    AccountClass = accounts.get(account_type.lower())
    if AccountClass is None:
        raise ValueError("Enter a valid account type")
    return AccountClass(holder_name, initial_deposit)


def transfer_funds(from_account, to_account, amount):
    """Transfer money between accounts"""
    from_account.withdraw(amount)
    to_account.deposit(amount)
    print("Your transaction was successful")


def generate_account_statement(account, start_date=None, end_date=None):
    """Generate formatted account statement"""
    transactions = account.transactions
    if start_date:
        transaction = [t for t in transactions if t["date"] >= start_date]
    if end_date:
        transaction = [t for t in transactions if t["date"] <= end_date]

    statement_lines = [
        f"Account statement for {account.account_holder}",
        f"Account number: {account._account_counter}",
        f"Account Balance: {account.initial_balance}",
        "-" * 40,
        f"{'Transaction Type':<20} {'Amount':<15} {'Date':<10}",
        "-" * 40
        ]
    for t in transaction:
        line = (
            f"{t['transaction_type']:<20} "
            f"{t['amount']:<15.2} "
            f"{t['date'].strftime('%Y-%m-%d %H:%M:%S'):<10}"
            )
        statement_lines.append(line)
    return "\n".join(statement_lines)


def find_accounts_by_holder(accounts_list, holder_name):
    """Find all accounts belonging to a specific holder"""
    return [account
            for account in accounts_list
            if account.account_holder.lower() == holder_name.lower()
            ]


# -----------------------------------------------------------
# Banking System Class
# -----------------------------------------------------------


class BankingSystem:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_deposits(self):
        deposits = 0
        for account in self.accounts:
            for transaction in account.transactions:
                if transaction["transaction_type"] == "deposit":
                    deposits += transaction["amount"]
        return deposits

    def get_accounts_summary(self):
        summary = []
        for account in self.accounts:
            summary.append({
                "Account Holder": account.account_holder,
                "Account Number": account._account_counter,
                "Account Balance": account.initial_balance,
                "Number of transactions": len(account.transactions)
                })
        return summary
