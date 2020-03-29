#Write a function that accepts a number x and evaluates the following expression:

#y=sin(x)−cos(x)+sin(x)cos(x)

#and returns the value of y. (Hint: Use math module)
from math import *
def trionometric(x):
    y=abs(x**3)+cos(sqrt(3*x))
    return y
