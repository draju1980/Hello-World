# Write a function that takes a two-dimensional list (list of lists) of numbers 
# as argument and returns a list which includes the sum of each column. Assume 
# that the number of columns in each row is the same.


def _sum_of_columns_sample_(sample_list):
    # Solution type 1:
    # return [max(col) for col in zip(*sample_list)]
    # Alternative Solution
    cols = len(sample_list[0])
    mylist = []
    #for c in range(cols):
        #column_sum = 0
        #for row in sample_list:
            #column_sum += row[c]
        #mylist.append(column_sum)
    for i in range(cols):
        col_sum=0
        for row in sample_list:
            col_sum+=row[i]
        mylist.append(col_sum)
    return mylist



    


print("SUM : ",_sum_of_columns_sample_([[1, 2, 3, 5], [1, 5, 4, 5]]))