# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

legal_drinking_age = 18

class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def can_enter_nightclub(self):
    """Checks Person age against the LEGAL_DRINKING_AGE."""
    if self.age > legal_drinking_age:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")

person = Person(17.9)
can_enter_nightclub(person)
        
