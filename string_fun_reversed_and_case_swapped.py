# Write a function which accepts an input string and returns a reverse of the
# input string while the case for every single character is reversed. The input
# string for this function would be a sentence (words separated by spaces)
# consisting of alphabetic characters.
def string_reversed_case_swapped(input_string):
    output_string=input_string.swapcase()
    return output_string[::-1]

print(string_reversed_case_swapped("Hello Python World"))
