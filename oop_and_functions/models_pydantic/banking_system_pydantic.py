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
    
    def withdraw(self, amount):
        # Your implementation here  
        pass
    
    def get_balance(self):
        # Your implementation here
        pass
    
    def get_account_info(self):
        # Your implementation here
        pass
