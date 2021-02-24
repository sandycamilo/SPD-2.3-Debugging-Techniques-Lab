import math
import pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
  """Returns the estimated age of the sample in year.
  carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
  in the sample conpared to the amount in living 
  tissue (unitless). 
  """
  if carbon_14_ratio < 0:
    raise ValueError("Ratio can't be negative")
  return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

carbon_14_ratio = 0.35
print(get_age_carbon_14_dating(carbon_14_ratio))

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.
def test_get_age_carbon_14_dating():
  carbon_14_ratio = 0.35
  assert math.log(get_age_carbon_14_dating(carbon_14_ratio), 8680.34)

def test_special_case_get_age_carbon_14():
  with pytest.raises(ValueError):
    get_age_carbon_14_dating(0)