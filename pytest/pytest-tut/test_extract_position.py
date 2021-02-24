import pytest
import math
import extract_position

@pytest.fixture
def error():
  return "error x:21.432"

@pytest.fixture
def valid():
  return "x:21.432"

def test_extract_position(error, valid):
  assert extract_position.extract_position(error) == None
  assert extract_position.extract_position(valid) == "21.432"