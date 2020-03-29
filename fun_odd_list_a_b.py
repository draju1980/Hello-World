# Write a function that accepts two positive integers a and b
# (a is smaller than b)and returns a list that contains all the odd numbers between a and b
# (including a and including b if applicable) in descending order.

def even_list(a,b):
    mylist=[]
    even=0
    for i in range(a,b+1):
        if i%2!=0:
            mylist.insert(i,i)
    mylist.reverse()
    return mylist

