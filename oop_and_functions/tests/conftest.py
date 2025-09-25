import pytest
from banking_system_pydantic import Account, SavingsAccount, CheckingAccount, BusinessAccount

@pytest.fixture
def base_account():
    return Account(account_holder="Joe", initial_balance=500)

@pyest.fixture
def savings_account():
    return SavingsAccount(account_holder="Bob", initial_balance=1000)

@pytest.fixture
def checking_account():
    return CheckingAccount(account_holder="Carol", initial_balance=200)

@pytest.fixture
def business_account():
    return BusinessAccount(
        account_holder="Lily",
        business_name="Lily Beauty Products",
        initial_balance=3000
        )
