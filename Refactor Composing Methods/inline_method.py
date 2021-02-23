# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18

class Person:
    def __init__(self, my_age):
        self.age = my_age
        
    def can_enter_nightclub(self):
        """Checks Person age against the LEGAL_DRINKING_AGE."""
        if self.age >= LEGAL_DRINKING_AGE:
            print("Allowed to enter.")
        else:
            print("Enterance of minors is denied.")

person = Person(17.9)
person.can_enter_nightclub()
        
