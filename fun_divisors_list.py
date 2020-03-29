# Write a function that accepts a positive integer k and returns the
# list of all the divisors of k. Your list should include both 1 and k.

def divisors_list(k):
    mylist=[]
    for i in range(1,k+1):
        if k%i==0:
            mylist.insert(i,i)
    return mylist




