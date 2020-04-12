# Write a function that accepts a 2-dimensional list of integers, 
# and sorts (descending order) all the elements inside each row and 
# returns the sorted 2-dimensional list.

def _2d_rows_sorted_sample_(_2d_list):
    for rows in _2d_list:
        rows.sort(reverse=True)
    return _2d_list



    


print("Sort : ",_2d_rows_sorted_sample_([[1, 2, 3, 5], [1, 5, 4, 7]]))