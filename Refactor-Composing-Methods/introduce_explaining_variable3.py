# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)

def cooking_criteria_satisfied(time, temperature, pressure, state):
    """Checks if cooking criteria is satisfied"""
    cooking = time * temperature * pressure * 0.05

    if cooking >= states[state]:
        return True 
    return False

states = {
        'well_done_state': 900000,
        'medium_state': 600000,
    }
print(cooking_criteria_satisfied(12, 100, 180, 'medium_state'))