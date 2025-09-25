from pydantic import BaseModel, Field, validator, root_validator
from typing import ClassVar, Annotated, List, Dict, Optional
from __future__ import annotations
from datetime import datetime, date
import random


# --------------------------------------
# Account Class
# --------------------------------------
class Account(BaseModel):
    # Class variable for generating unique account numbers
    _account_counter: ClassVar[int] = 1000
    
    account_holder: str
    initial_balance: int = Field(default=0)
    account_number: int = Field(default_factory=lambda: Account._next_account_number())
    transaction_history = List[Dict] = Field(default_factory=list)

    class Config:
        validate_assignment = True

    @classmethod
    def _next_account_number(cls) -> int:
        cls._account_counter += 1
        return cls._account_counter

    @validator("initial_balance")
    def balance_must_be_number(cls, num):
        try:
            return int(num)
        except Exception:
            raise ValueError("Initial balance must be numeric")
    
    def deposit(self, amount: int):
       self.initial_balance += int(amount)
       self._record_transaction("Deposit", amount, description)
 
    def withdraw(self, amount: int) -> bool:
        if int(amount) > self.initial_balance:
            return False
        self.initial_balance -= int(amount)
        self._record_transaction("Withdrawal", amount, description)
        return True

    def _record_transaction(self, transaction_type: str, amount: int, description: str):
        transaction = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": transaction_type,
            "amount": int(amount),
            "description": description,
            "balance": int((self.initial_balance)
                           }
            self.transaction_history.append(transaction)
            return transaction
    
    def get_balance(self) -> int:
        return int(self.initial_balance)
    
    def get_account_info(self) -> str:
        return (
            f"Account Holder: {self.account_holder}\n"
            f"Account Balance: {self.initial_balance}\n"
            f"Transaction: {self.transaction_history}"
            )


# ---------------------------
# Savings Account Class
# ---------------------------
class SavingsAccount(Account):
    minimum_balance: int = 100
    monthly_interest_rate = 0.5 / 100

    def withdraw(self, amount: int) -> int:
        withdraw_amount = self.initial_balance - int(amount)
        if withdraw_amount < self.minimum_balance:
            return False
        self.initial_balance = withdrawal_amount
        self._record_transaction("Withdrawal", amount, description)
        return True

    def apply_monthly_interest(self):
        interest = self.initial_balance * self.monthly_interest_rate / 12
        if interest > 0:
            self.initial_balance += interest
            self._record_transaction("Interest", interest, "Monthly interest applied")
        return interest

    def get_account_type(self):
        return "Savings Account"


# ----------------------------
# Checking Account
# ----------------------------
class CheckingAccount(Account):
    overdraft_fee: int = 2
    overdraft_limit: int = 500
    
    def withdraw(self, amount: int) -> bool:
        amount = int (amount)
        projected_balance = self.initial_balance - amount
        if projected_balance < -self.overdraft_limit:
            return False
        self.initial_balance = projected_balance
        if self.initial_balance < 0:
            self.initial_balance -= self.overdraft_fee
            self._record_transaction("Fee", self.overdraft_fee, "Overdraft fee applied")
        self._record_transaction("Withdrawal", amount, description)
        return True

    def get_overdraft_available(self) -> int:
        return int(self.overdraft_limit + min(self.initial_balance, 0))

    def get_account_type(self):
        return "Checking Account"


# ----------------------------------
# Business Account Class
# ----------------------------------
class BusinessAccount(Account):
    overdraft_limit: int = 2000
    overdraft_fee: int = 5
    business_name: str = ""

    @root_validator(pre=True)
    def ensure_business_name(cls, value):
        if not value.get("business_name"):
            raise ValueError("Business name is required")
        return value

    def withdraw(self, amount: int) -> bool:
        amount = int (amount)
        projected_balance = self.initial_balance - amount
        if projected_balance < -self.overdraft_limit:
            return False
        self.initial_balance = projected_balance
        if self.initial_balance < 0:
            self.initial_balance -= self.overdraft_fee
            self._record_transaction("Fee", self.overdraft_fee, "Overdraft fee applied")
        self._record_transaction("Withdrawal", amount, description)
        return True
    
    def get_account_type(self) ->:
        return "Business Account"


# ----------------------------------------------
# Card System
# ----------------------------------------------
class Card(BaseModel):
    card_number: str = Field(default_factory=lambda:"".join(str(random.randint(0, 9)) for _ in range (16)))
    linked_account: Account
    card_type:str
    is_active: bool = True

    class Config:
        arbitrary_types_allowed = True

    def make_purchase(self, amount: int, merchant: str) -> bool:
        if not self.is_active:
            return False
        return self.linked_account.withdraw(amount)

    def get_card_info(self) -> str:
        return (
            f"Card #{self.card_number}\n"
            f"Type: {self.card_type}\n"
            f"Linked Account: {self.linked_account.account_number}\n"
            f"Active: {self.is_active}"
            )


# ----------------------------------------
# Debit Card
# ----------------------------------------
class DebitCard(Card):
    daily_limit: int = 1000
    _daily_spent: int = 0
    _daily_spent_date: date = Field(default_factory=lambda:date.today())

    def make_purchase(self, amount: int, merchant: str) -> bool:
        today = date.today()
        if today !== self._daily_spent_date:
            self._daily_spent = 0
            self._daily_spent_date = today
        if self._daily_spent + amount > self.daily_limit:
            return False
        success = self.linked_account.withdraw(amount)
        if success:
            self._daily_spent += int(amount)
            return True
        return False

# ----------------------------------------------
# Credit Card
# ----------------------------------------------
class CreditCard(Card):
    credit_limit: int = 5000
    current_balance: int = 0

    def make_purchase(self, amount: int, merchant: str) -> bool:
        available = self.credit_limit - self.current_balance
        if amount > available:
            return False
        self.current_balance += int(amount)
        self.linked_account._record_transaction(
            "Credit Charge", amount, f"Credit Card Charge at {merchant}\n(Card No: {self.card_number[-4:]})"
            )
            return True

    def make_payment(self, amount: int) -> bool:
        if self.linked_account.get_balance() < amount:
            return False
        success = self.linked_account.withdraw(amount)
        if not success:
            return False
        self.current_balance = max(0, self.current_balance - amount)
        self.linked_account_record_transaction("Credit card payment", amount, f"Credit Card {self.card_number[-4:]}")
        return True


# ----------------------------------------
# Banking System
# ----------------------------------------
class BankingSystem(BaseModel):
    bank_name: str
    accounts: List[Account] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def add_account(self, account: Account):
        self.accounts.append(account)

    def get_total_deposits(self) -> int:
        return sum(max(0, a.get_balance()) for a in self.accounts)

    def get_accounts_summary(self) -> List[Dict]:
        return [
            {
                "account_number": a.account_number,
                "holder": a.account_holder,
                "type": a.get_account_type(),
                "balance": a.get_balance(),
            }
            for a in self.accounts
        ]
