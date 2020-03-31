# Write a function that accepts an input string consisting of alphabetic
# characters and removes all the trailing whitespace of the string and returns
# it without using any .strip() method.
def _remove_trailing_whitespace_sample_(string):
    my_index = None
    i = len(string)
    while i > 0:
        if string[i-1] != " ":
            my_index = i
            break
        i = i - 1
    # slice the string from 0 to that index
    new_string = string[:my_index]
    return new_string
print(_remove_trailing_whitespace_sample_("    Hello  "))
    
