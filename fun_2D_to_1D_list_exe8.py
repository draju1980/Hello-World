# Write a function that accepts a 2-dimensional list of integers, and returns 
# a sorted (ascending order) 1-Dimensional list containing all the integers 
# from the original 2-dimensional list.

def _2d_to_1d_list_sample_(_2d_list):
    output_list = []
    for rows in _2d_list:
        for items in rows:
            output_list.append(items)
    output_list.sort()
    return output_list



    


print("MAX : ",_max_of_columns_sample_([[1, 2, 3, 5], [1, 5, 4, 7]]))