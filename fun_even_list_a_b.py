# Write a function that accepts two positive integers a and b and returns a
# list of all the even numbers between a and b (including a and not including b).
def even_list(a,b):
    mylist=[]
    even=0
    for i in range(a,b+1):
        if i%2==0:
            mylist.insert(i,i)
    return mylist

