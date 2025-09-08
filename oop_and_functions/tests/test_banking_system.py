#!/usr/bin/python3
"""These are tests for the banking system app"""
import unittest
import datetime
import time
from models.banking_system import Account
from models.banking_system import SavingsAccount
from models.banking_system import BusinessAccount
from models.banking_system import CheckingAccount


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.my_account = Account("Joe", 9000)

    def test_account_holder_name(self):
        self.assertEqual(self.my_account.account_holder, "Joe")

    def test_account_balance(self):
        self.assertEqual(self.my_account.initial_balance, 9000)
