# Write a function that will receive a 2D list of integers. The function 
# should return the count of how many rows of the list have even sums and the 
# count of how many rows have odd sums. For example if the even count was 2, 
# and odd count was 4 your function should 
# return them in a list like this: [2, 4].


def _count_even_sum_sample_(sample_2d_list):
    even_count = 0
    odd_count = 0
    # For each row
    for rows in sample_2d_list:
        row_sum = sum(rows)
        if row_sum % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return [even_count, odd_count]



    


print("SUM : ",_count_even_sum_sample_([[1, 2, 3, 5], [1, 5, 4, 5]]))