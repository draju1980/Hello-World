# Write a function that accepts a list and returns a new list such that the
# new list contains all the items of the old list in reverse order.
# Note that this is NOT a sorting problem.
def _reverse_of_a_list_sample_(old_list):
    new_list = []
    length = len(old_list)
    i = -1
    # Iterate the list using negative indices
    while i >= -length:
        new_list.append(old_list[i])
        i = i - 1
    return new_list
