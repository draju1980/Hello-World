# Write a function that accepts a list and a value of an element and returns the count of how many times that element appears in the list.
def _list_manipulation_sample3_(input_list, k):
    my_Count = 0
    for element in input_list:
        if element == k:
            my_Count = my_Count + 1
    return my_Count
