# Write a function that accepts an input string consisting of alphabetic
# characters and removes all the leading whitespace of the string and returns
# it without using .strip().
def string_exe1(input_string):
    new_string=None
    for i in range(0,len(input_string)):
        if input_string[i] !=" ":
            temp_string=i
            break
    new_string=input_string[temp_string::]
    return new_string
print(string_exe1("    Hello  "))
    
