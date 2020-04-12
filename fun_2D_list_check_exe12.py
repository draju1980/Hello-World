# Write a function that accepts two (matrices) 2 dimensional lists a and b of 
# unknown lengths and returns their product. Hint: Two matrices a and b can be 
# multiplied together only if the number of columns of the first matrix(a) is the 
# same as the number of rows of the second matrix(b). Hint: You may import and 
# use the numpy module but your return must be a python list not a numpy array. 
# The input for this function will be two 2 Dimensional lists.

#Solution 1 with numpy
def _product_of_two_vectors_sample_(a, b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))     
    # returns a numpy array
    product_to_list = product.tolist()          
    # convert the numpy array to a standard list
    return product_to_list

# Solution 2 with out numpy
def _product_of_two_vectors_sample_(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list



    


print("Sort : ",_multiplication_check_sample_([[2, 3, 4, 5], [3, 4, 5, 1]], [[4, -3, 12], [1, 1, 5], [1, 3, 2]]))