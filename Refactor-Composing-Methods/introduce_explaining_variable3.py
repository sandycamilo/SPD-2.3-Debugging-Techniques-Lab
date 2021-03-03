# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)

WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def cooking_criteria_satisfied(time, temperature, pressure, desired_state):
    """Checks if cooking criteria is satisfied"""
    states = {
        'well_done_state': WELL_DONE,
        'medium_state': MEDIUM,
    }
  
    cooking = time * temperature * pressure * COOKED_CONSTANT

    if cooking >= states[desired_state]:
        return True 
    return False

print(cooking_criteria_satisfied(12, 100, 180, 'medium_state'))