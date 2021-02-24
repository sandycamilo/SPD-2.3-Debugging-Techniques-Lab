import math
import pytest

def calculate_kinetic_energy(mass, velocity):
  """Returns kinetic energy of mass [kg] with velocity [ms]."""
  return 0.5 * mass * velocity ** 2

# writing a failing test 
# someone mistakenly removes 0.5 in the kinetic energy formula as follows
# gives an assertion error
# def calculate_kinetic_energy(mass, velocity): 
#   """Returns kinetic energy of mass [kg] with velocity [ms]."""
#   return mass * velocity ** 2

# test 
def test_calculate_kinetic_energy():
  mass = 10 # [kg]
  velocity = 4 # [m/s]
  # math.isclose is a method that checks whether two values are close to each other
  assert math.isclose(calculate_kinetic_energy(mass, velocity), 80)

# practice 1
def get_average(li):
  sum = 0
  for num in li:
    sum += num
  mean = sum / len(li)
  return mean

# test for practice 1  
def test_get_average():
  li = [1,4,5,6]
  assert math.isclose(get_average(li), 4.0)

# practice 2  
def palindrome(word):
  """checks whether a word is a palindrome or not."""
  if not isinstance(word, str):
    raise TypeError('Please provide a string argument')
  return word == word[::-1]

# unit test for practice 2 - exception
def test_palindrome():
  with pytest.raises(TypeError):
    palindrome(44)