import pytest
import math
import calculate_stat 
from numpy.testing import assert_almost_equal

def test_calculate_stat():
  mean, sd = calculate_stat.calculate_stat([12, 23, 45, 67, 74])
  # assert  math.isclose(44.2, mean)
  # assert math.isclose(24.062, sd)
  assert_almost_equal(mean, 44.2, decimal=1)
  assert_almost_equal(sd, 24.062, decimal=3)