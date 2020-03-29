# Write a function that accepts two lists both of which consists of integers
# and returns the total sum of all the odd integers from both lists.
def list_exe8(lista,listb):
    newlist=[]
    total=0
    for item in lista:
        if item%2!=0:
            newlist.append(item)
    for item in listb:
        if item%2!=0:
            newlist.append(item)
    for item in newlist:
        total=total+item
    return total
