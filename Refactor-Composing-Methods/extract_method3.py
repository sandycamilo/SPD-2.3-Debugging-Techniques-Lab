# # Written by Kamran Bigdely
# # Example for Compose Methods: Extract Method. 
# # Find the duplicate logic and extract a method for it.

import math

def calcualte_circle_distance(x1, x2, y1, y2): 
    """Calculates the distance between two circles."""
    distance = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    return distance

x1 = 4
y1 = 4.25
x2 = 53
y2 = -5.35
distance = calcualte_circle_distance(x1, x2, y1, y2)
print('Distance:', distance)


def calculate_vector(x1, x2, y1, y2):
    """Calcualtes the length vector between A and B points."""
    length = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    return length

x1 = -36
y1 = 97
x2 = .34
y2 = .91
length = calculate_vector(x1, x2, y1, y2)
print('Length:', length)