def test_business_higher_overdraft(business_account):
    success = business_account.withdraw(4500)
    assert success
    assert business_account.get_balance() < 0
    assert any(t["type"] == "Fee" for t in business_account.transaction_history)

def test_business_info_includes_name(business_account):
    info = business_account.get_account_info()
    assert "Lily Beauty products" in info

