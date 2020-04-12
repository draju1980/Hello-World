# Write a function that takes a two-dimensional list (list of lists) of numbers 
# as argument and returns a list which includes the sum of each row. You can 
# assume that the number of columns in each row is the same.


def _sum_of_2d_list(input_list):
    total=[]
    for element in input_list:
        total.append(sum(element))     
    return total

#def _sum_of_rows_sample_(sample_list):
#    mylist = []
#    for item in sample_list:
#        mylist.append(sum(item))
#    return mylist

print("Max : ",_sum_of_2d_list([[1, 2, 3, 5], [1, 5, 4, 5]]))