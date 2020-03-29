# Write a function that accepts a positive integer k and returns the ascending sorted list of
# cube root values of all the numbers from 1 to k (including 1 and not including k).
# [if k is 1, your program should return an empty list]

def cube_list(k):
    mylist=[]
    for i in range(1,k):
        sr=i**(1/3)
        mylist.insert(i,sr)
    return mylist




