# Write a function named list_of_primes that accepts a positive integer n
# and returns a sorted list (ascending order)
def list_of_primes_sample(n):
    my_list = []
    integer = 2
    while integer < n:
        prime = True
        start = 2
        while start < integer:
            if integer % start == 0:
                prime = False
            start = start + 1
        if prime == True:
            my_list.append(integer)
        integer = integer + 1
    return my_list
print(list_of_primes_sample(5))
            

