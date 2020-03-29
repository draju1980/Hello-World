# Write a function named crazy_list that accepts a list as parameter and
# returns a boolean (either True or False) based on whether or not the list
# is the same forward and backwards.
# Type your code here
def crazy_list(some_list):
    if some_list==some_list[::-1]:
        return True
    else:
        return False
