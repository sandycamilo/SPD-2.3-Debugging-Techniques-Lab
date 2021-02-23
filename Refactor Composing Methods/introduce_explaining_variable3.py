# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)

WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def cooking_criteria_satisfied(time, temperature, pressure):
    """Checks if cooking criteria is satisfied"""
    well_done_state = 'well-done'
    medium_state = 'medium'
    cooked = time * temperature * pressure * COOKED_CONSTANT
    if well_done_state and cooked >= WELL_DONE:
        return True 
    if medium_state and cooked >= MEDIUM:
        return True
    return False
