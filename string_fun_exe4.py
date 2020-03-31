# Write a function which accepts an input string consisting of alphabetic
# characters and spaces and returns the string with all the spaces removed

def string_fun_exe4(s):
    output_string=""
    for i in range(0,len(s)):
        if s[i]!=" ":
            output_string=output_string + s[i]
    return output_string
print(string_fun_exe4("    Hello  "))
    
