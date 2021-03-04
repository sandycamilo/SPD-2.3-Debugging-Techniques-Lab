# by Kami Bigdely 
# Replace magic numbers with named constanst

# First Section
# Given two point charges, calcualte the electric force exerted on them.
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))
FORCE = 8.9875517923*1e9

def calcualte_force():
    force = FORCE * q1 * q2/(distance**2)
    print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
NUM = int(input('Enter an integer number: ')) % 2
if NUM == 0:
    print(NUM, "is an even number.")
else:
    print(NUM, "is an odd number.")