# Write a function that accepts two positive integers as parameters.
# The first integer is the number of heads and the second integer is the number of legs of all the creatures
# in a farm which consists of chickens and dogs.

def solve(numHeads,numLegs):
    for numChicks in range(0, numHeads + 1): 
        numDogs = numHeads - numChicks 
        totLegs = 4 * numDogs + 2* numChicks 
        if totLegs == numLegs: 
           return [numChicks,numDogs] 
    return None
    
    
