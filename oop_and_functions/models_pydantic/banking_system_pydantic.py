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
            f"Account Balance: {self.initial_balance}"
            f"Transaction: {self.transaction_history}"
            )

class SavingsAccount(Account):
    interest_rate :ClassVar[int] = 1.005
    
    initial_balance : int = 100

    def withdraw(self, amount: int):
        balance = self.initial_balance
        floor_balance = 100
        
        if balance - withdraw < floor_balance:
            return False
        self.initial_balance -= amount
        return True

    def apply_monthly_interest(self):
        self.initial_balance * self.__class__.interest_rate
        return self.initial_balance

    def get_account_type(self):
        return f"Savings Account"

class CheckingAccount(Account):
    overdraft_fee :ClassVar[int] = 2
    
    def withdraw(self, amount: int):
        balance = self.initial_balance

        if balance - withdraw < balance:
            return False
        self.initial_balance -= amount
        return True

    def apply_monthly_interest(self):
        self.initial_balance * self.__class__.interest_rate
        return self.initial_balance

    def get_account_type(self):
        return f"Checking Account"
