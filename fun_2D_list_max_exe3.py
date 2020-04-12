# Write a function that accepts a 2D list of integers and returns the maximum 
# EVEN value for the entire list. You can assume that the number of columns in 
# each row is the same. Your function should return None if the list is empty 
# or all the numbers in the 2D list are odd.


def _maximum_even_value_sample_(sample_2d_list):
    if not sample_2d_list: # list is empty
        return None
    result=None
    for row in sample_2d_list:
        row_max=_max_even_of_1d_list(row)
        if row_max:
            if result==None or row_max>result:
                result=row_max
    return result

def _max_even_of_1d_list(input_list):
    result=None
    for element in input_list:
        if element%2 ==0: # if element is even
            if result==None or element>result:
                result=element
    return result

print("Max : ",_maximum_even_value_sample_([[1, 2, 3, 5], [1, 5, 4, 5]]))