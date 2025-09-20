from pydantic import BaseModel
from typing import ClassVar

class Account:
    # Class variable for generating unique account numbers
    _account_counter = ClassVar[int] = 1000
    
    account_holder: str
    initial_balance: int = 0
    
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
