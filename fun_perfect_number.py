# Write a function that receives a positive integer as function parameter
# and returns True if the integer is a perfect number,False otherwise.
# A perfect number is a number whose sum of the all the divisors
# (excluding itself) is equal to itself.
def perfect_number(n):
    perfect=0
    for item in range(1,n):
        if n % item == 0:
            perfect+=item
    return bool(perfect==item)

        
