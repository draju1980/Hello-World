# Write a function which accepts an input list of numbers
# and returns the largest number in the list (Do not use python's built-in max() function). 
def list_max(mylist):
    maxn=mylist[0]
    for item in mylist:
        if item > maxn:
            maxn = item
    return maxn
