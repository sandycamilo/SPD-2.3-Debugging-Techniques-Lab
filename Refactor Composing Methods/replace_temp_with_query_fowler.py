# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.

def get_price():
    return base_price() * discount_factor()

def base_price():
    return quantity * item_price

def discount_factor():
    if base_price() > 1000: 
        return 0.95
    return 0.98

