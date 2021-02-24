# test_wallet.py
# rewrite using fixtures - to shorten tests 
# fixure functions are wallet() and empty_wallet()
# @pytest.fixture decorator is used to tell pytest that a function is a fixture

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
  """Returms a Wallet instance with a zero balance."""
  return Wallet()

@pytest.fixture
def wallet():
  """Returns a Wallet instance with a balance of 20."""
  return Wallet(20)

def test_default_initial_amount():
  assert wallet.balance == 0

def test_setting_initial_amount():
  assert wallet.balance == 20

def test_wallet_add_cash():
  wallet.add_cash(80)
  assert wallet.balance == 100

def test_wallet_spend_cash():
  wallet.spend_cash(10)
  assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
  with pytest.raises(InsufficientAmount):
    wallet.spend_cash(100)