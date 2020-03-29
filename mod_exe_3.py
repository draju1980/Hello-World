#Write a function that finds the distance between two points and returns it.
#The distance between two points with x,y, and z components can be calculated as: 
#distance=√(x2−x1)2+(y2−y1)2+(z2−z1)2
#The input for this function will be two 1 Dimensional lists that contain the x,y,z coordinates each.
#For example if the input lists are: 
# a = [2, 3, -5] 
# b = [4, -3, 12]
# Then your function should return their distance such as:
# 18.138357147217054


from math import *
def distance_calc(lista,listb):
    x1=lista[0]
    x2=listb[0]
    y1=lista[1]
    y2=listb[1]
    z1=lista[2]
    z2=listb[2]
    distance=(sqrt((x2-x2)**2+(y2-y1)**2+(z2-z1)**2))
    return distance
