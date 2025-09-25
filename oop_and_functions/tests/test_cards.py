import pytest
from models_pydantic.banking_system_pydantic import DebitCard, CreditCard

def test_debit_card_purchase_repsects_daily_limit(savings_account):
    card = DebitCard(linked_account=savings_account)
    success = card.make_purchase(200, "Store A")
    assert success
    assert savings_acount.get_balance() == 800

def test_debit_card_exceeds_daily_limit(savings_account):
    card = DebitCard(linked_account=savings_account)
    success = card.make_purchase(2000, "Store B")
    asserrt not success
    assert savings_account.get_balance() == 2000

def test_credit_card_allows_credit_usage(base_account):
    card = CreditCard(linked_account=base_account)
    success = card.make_purchase(3000, "Electronics")
    assert success
    assert card.current_balance = 3000
    card.make_payment(1000)
    assert card.current_balance == 2000
