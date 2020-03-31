# Write a function that takes a list of words as an input argument and
# returns True if the list is sorted and returns False otherwise.
def _is_sorted_sample_(sample_list):
    # Create a copy of the sample_list using list slicing
    copy_original = sample_list[:]
    # Sort the sample list using python's built in sort() method
    sample_list.sort()
    # Compare the original list with the now sorted list to see if they are equal
    if copy_original == sample_list:
        return True     # Sample list was already sorted
    else:
        return False    # Sample list was not sorted
print(_is_sorted_sample_(['p', 'r', 's', 't', 'u', 'a']))
