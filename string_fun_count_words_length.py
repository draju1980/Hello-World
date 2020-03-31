# Write a function that accepts a string and a character as input and returns
# the count of all the words in the string which start with the given character.
# Assume that capitalization does not matter here. You can assume that the input
# string is a sentence i.e. words are separated by spaces and consists of
# alphabetic characters.
def _count_of_words_sample_(input_string):
    # Create a list of strings by splitting the original string
    splitted_string = input_string.lower().split()
    # set the maximum length
    maximum_length = 4
    # Go through each string in the list we created
    count = 0
    for string in splitted_string:
        # check the length of each string
        #  it resets for each string
        string_length = len(string)
        if string_length > maximum_length:
            count = count + 1
    return count

print(_count_of_words_sample_("Hello World"))
    
