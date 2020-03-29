# Write a function that accepts two input lists and returns a
# new list which contains only the unique elements from both lists.
def list_eve9(lista,listb):
    newlist=[]
    for itema in lista:
        if itema not in newlist:
            newlist.append(itema)
    for itemb in listb:
        if itemb not in newlist:
            newlist.append(itemb)
    return newlist

print(list_eve9([1, 2, 3, 4, 5, 6], [5, 5, 6, 2, 8]))
    
        
