from pydantic import BaseModel, Field, conint
from typing import ClassVar, Annotated


class amount_greater_than_zero(BaseModel):
    amount : int = Field(gt=0)

class Account(BaseModel):
    # Class variable for generating unique account numbers
    _account_counter: ClassVar[int] = 1000
    
    account_holder: str
    initial_balance: int = Field(default=0)
    
    def deposit(self, amount: int):
       validated = amount_greater_than_zero(amount=amount)
       self.initial_balance += validated.amount
       return amount
    
    def withdraw(self, amount):
        validated = amount_greater_than_zero(amount=amount)
        if self.initial_balance < validated.amount:
            return False    
        self.initial_balance -= validated.amount
        return True
    
    def get_balance(self):
        return self.initial_balance
    
    def get_account_info(self):
        return (
            f"Account Holder: {self.account_holder}\n"
            f"Account Balance: {self.initial_balance}"
            )
