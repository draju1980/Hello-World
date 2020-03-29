# Write a function that accepts a list that contains positive integers and returns a new list which
# contains all the elements from original list but adds 1 to those elements which are odd.
def list_exe7(mylist):
    newlist=[]
    for items in mylist:
        if items%2==0:
            newlist.insert(items,items)
        else:
            newlist.insert(items,items+1)
    return newlist
