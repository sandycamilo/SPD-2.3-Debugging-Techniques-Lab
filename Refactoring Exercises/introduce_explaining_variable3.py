# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)

well_done = 900000
medium = 600000
cooked_constant = 0.05

def cooking_criteria_satisfied(time, temperature, pressure):
    well_done_state = 'well-done'
    medium_state = 'medium'
    cooked = time * temperature * pressure * cooked_constant
    if well_done_state and cooked >= well_done:
        return True 
    if medium_state and cooked >= medium:
        return True
    return False
