# Write a function that takes a two-dimensional list (list of lists) of numbers 
# as argument and returns a list which includes the maximum value of each 
# column. Assume that the length of columns is consistent in each row.

def _max_of_columns_sample_(sample_list):
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_max = 0
        for row in sample_list:
            if row[c] > column_max:
                column_max = row[c]
        mylist.append(column_max)
    return mylist



    


print("MAX : ",_max_of_columns_sample_([[1, 2, 3, 5], [1, 5, 4, 7]]))