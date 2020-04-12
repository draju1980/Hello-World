# Write a function that takes a two-dimensional list (list of lists) of 
# numbers as argument and returns a list which includes the 
# maximum value of each row.


def _max_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(max(item))
    return mylist



    


print("MAX : ",_max_of_rows_sample_([[1, 2, 3, 5], [1, 5, 4, 7]]))