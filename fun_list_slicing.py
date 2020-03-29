# Write a function that accepts a list as input and returns a new list which includes every
# other element in the original list. Keep the first element, i.e. input_list[0].
def _every_other_element_sample_(sample_list):
    output = []
    length = len(sample_list)
    output.append(sample_list[0])
    for element in range(1, length):
        if element % 2 == 0:
            output.append(sample_list[element])
    return output 
