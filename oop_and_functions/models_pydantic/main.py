from pydantic import BaseModel

class Account(BaseModel):
    # Class variable for generating unique account numbers
    _account_counter = 1000
    
    def __init__(self, account_holder, initial_balance=0):
        # Your implementation here
        pass
    
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
