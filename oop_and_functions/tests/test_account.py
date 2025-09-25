from banking_system_pydantic import Account

def test_deposit_invreses_balance(base_account):
    base_account.deposit(200)
    assert base_account.get_balance() == 700
    assert base_account.transaction_history[-1]["type"] == "Deposit"

def test_withdraw_success(base_account):
    success = base_account.withdraw(100)
    assert success
    assert base_account.get_balance() == 400
    assert base_account.transaction_history[-1]["type"] == "Withdrawal"

def test_withdraw_fails_on_insufficient(base_account):
    success = base_account.withdraw(1000)
    assert not success
    assert base_account.get_balance() == 500
