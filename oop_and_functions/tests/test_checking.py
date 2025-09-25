def test_checking_allows_overdraft(checking_account):
    success = checking_account.withdraw(600)
    assert success
    assert checking_account.get_balance() < 0
    assert any(t["type"] == "Fee" for t in checking_account.transaction_history)

def test_checking_denies_excessive_overdraft(checking_account):
    success = checking_account.withdraw(1000)
    assert not success
    assert checking_account.get_balance() == 200
