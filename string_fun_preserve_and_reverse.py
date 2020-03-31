# Write a function that accepts a string of words separated by spaces
# consisting of alphabetic characters and returns a string such that
# each word in the input string is reversed while the order of the words
# in the input string is preserved. The length of the input string must
# be equal to the length of the output string i.e. there should be no extra
# trailing or leading spaces in your output string

def _preserve_and_reverse_sample_(string):
    splitted_list = string.split()
    for x in range(0, len(splitted_list)):
        splitted_list[x] = splitted_list[x][::-1]
    # Initialize an output string
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "
    # Strip any white spaces
    output_string = output_string.strip()
    return output_string

print(_preserve_and_reverse_sample_("Hello Python World"))
