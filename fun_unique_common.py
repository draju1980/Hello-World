# Write a function named unique_common that accepts two lists both of which
# contain integers as parameters and returns a sorted list (ascending order)
# which contains unique common elements from both the lists. If there are no
# common elements between the two lists, then your function should return the
# keyword None

def unique_common(a, b):
    d=[]
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                d.append(a[i])
    d = list(dict.fromkeys(d))
    d.sort()
    return d

print(unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))
    
        
        
