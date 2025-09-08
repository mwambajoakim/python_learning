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
        self.checking = CheckingAccount("Joe", 500)

    def test_withdrawal_within_amount(self):
        result = self.checking.withdraw(80)
        self.assertTrue(result)

    def test_withdrawal_overdraft(self):
        result = self.checking.withdraw(600)
        self.assertTrue(result)
        self.assertEqual(self.checking.get_balance(), -102)

    def test_get_overdraft_available(self):
        self.checking.withdraw(700)
        overdraft_amount = self.checking.get_overdraft_available()
        self.assertEqual(overdraft_amount, 298)

class TestBusinessAccount(unittest.TestCase):
    def setUp(self):
        self.business = BusinessAccount("Joe", "Mwamba Ltd", 300)

    def test_withdrawal_within_amount(self):
        result = self.business.withdraw(80)
        self.assertTrue(result)

    def test_withdrawal_overdraft(self):
        result = self.business.withdraw(600)
        self.assertTrue(result)
        self.assertEqual(self.business.get_balance(), -305)

    def test_get_overdraft_available(self):
        self.business.withdraw(700)
        overdraft_amount = self.business.get_overdraft_available()
        self.assertEqual(overdraft_amount, 1595)

class TestValidateAmount(unittest.TestCase):
    def test_amount_less_than_zero(self):
        with self.assertRaises(ValueError) as err:
            validate_amount(-900)
            self.assertEqual(err.exception, "Amount must be a positive number and reasonable")

    def test_amount_more_than_a_million(self):
        with self.assertRaises(ValueError) as err:
            validate_amount(1000001)
            self.assertEqual(err.exception, "Amount must be a positive number and reasonable")

class TestCalculateInterest(unittest.TestCase):
    def test_simple_interest(self):
        simple_interest = calculate_interest(100, 2, 10)
        self.assertEqual(simple_interest, 20)

class TestFormatCurrency(unittest.TestCase):
    def test_currency_format(self):
        formatted_amount = format_currency(1000000)
        self.assertEqual(formatted_amount, 1,000,000)
