#!/usr/bin/python3
"""These are tests for the banking system app"""
import unittest
import datetime
import time
from models.banking_system import (
    Account, SavingsAccount, BusinessAccount, CheckingAccount, validate_amount,
    calculate_interest, format_currency, generate_transaction_id, Card,
    DebitCard, CreditCard, create_account, transfer_funds, generate_account_statement,
    find_accounts_by_holder, BankingSystem
    )


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.my_account = Account("Joe", 9000)

    def test_account_holder_name(self):
        self.assertEqual(self.my_account.account_holder, "Joe")

    def test_account_balance(self):
        self.assertEqual(self.my_account.initial_balance, 9000)

    def test_deposit(self):
        self.my_account.deposit(4000)
        self.assertEqual(self.my_account.get_balance(), 13000)

    def test_withdraw(self):
        result = self.my_account.withdraw(3000)
        self.assertTrue(result)
        self.assertEqual(self.my_account.get_balance(), 6000)

    def test_get_balance(self):
        balance = self.my_account.get_balance()
        self.assertEqual(balance, 9000)


class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.savings = SavingsAccount("Joe Save")

    def test_initial_balance(self):
        self.assertEqual(self.savings.get_balance(), 100)

    def test_savings_deposit(self):
        self.savings.deposit(500)
        self.assertEqual(self.savings.get_balance(), 600)
        self.assertEqual(self.savings.transactions[-1]["transaction_type"], "deposit")

    def test_withdraw(self):
        result = self.savings.withdraw(50)
        self.assertFalse(result)
        self.assertEqual(self.savings.get_balance(), 100)

    def test_apply_monthly_interest(self):
        interest_result = self.savings.apply_monthly_interest()
        self.assertEqual(interest_result, 100.5)

    def test_account_type(self):
        self.assertIsInstance(self.savings.get_account_type(), str)

class TestCheckingAccount(unittest.TestCase):
    def setUp(self):
        checking = CheckingAccount("Joe", 500)
