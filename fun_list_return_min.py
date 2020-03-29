# Write a function which accepts an input list of numbers and returns the smallest number in the list
#(Do not use python's built-in min() function).
def list_min(my_list):
    my_min=[]
    for item in my_list:
        my_min.append(item)
        my_min.sort()
    return my_min[0]
