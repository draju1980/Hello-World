# Write a function named items_price that accepts two lists as parameters.
# The first list contains the quantities of n different items, the second list
# contains the prices that correspond to those n items respectively. Now,
# calculate the total amount of money required to
# purchase those items. Assume that both the lists will have equal lengths

def items_price(a,b):
    c=[]
    total=0
    for a1,b1 in zip(a,b):
        c.append(a1*b1)
    for i in c:
        total = total + i
    return total
print(items_price([2, 3, 5, 7, 9],[5, 8, 4, 1, 11]))
