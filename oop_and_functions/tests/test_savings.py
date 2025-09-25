def test_saings_prevents_below_minimu(savings_account):
    success = savings_account.withdraw(950)
    assert not success
    assert savings_account.get_balance() == 1000

def test_apply_monthly_interest(savings_account):
    old_balance = savings_account.get_balance()
    interest = savings_account.apply_monthly_interest()
    assert > 0
    assert savings_account.get_balance() == old_balance + interest
