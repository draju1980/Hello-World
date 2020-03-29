# Write a function that accepts an input list and returns a new list which
# contains only the unique elements(Elements should only appear one time in the 
# list and the order of the elements must be preserved as the original list. )
def list_eve9(mylist):
    newlist=[]
    for item in mylist:
        if item not in mylist:
            newlist.append(item)
    return mylist

    
        
