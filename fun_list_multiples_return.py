# Write a function that accepts a positive integer k and
# returns a list that contains the first five multiples of k.
# The multiples should be calculated starting from 1 to 5 (including both 1 and 5).
# For example the first five multiples of 3 are 3, 6, 9, 12, and 15
def list_multiple(k):
    mylist=[]
    for i in range(1,6):
        mylist.insert(i,i*k)
    return mylist
        
