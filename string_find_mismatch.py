#Write a function named find_mismatch that accepts two strings as input arguments and returns:

# 0 if the two strings match exactly.
# 1 if the two strings have the same length and mismatch in only one character.
# 2 if the two strings do not have the same length or mismatch in two or more characters.
#Capital letters are considered the same as lower case letters. Here are some examples:
#First string	    Second String	Function return
# Python	    Java	        2
# Hello There	    helloothere	        1
# sin	            sink	        2 (note not the same length)
# dog	            Dog	                0

################### Instructor function ###################
def find_mismatch(s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 2
    return number_of_mismatches
        
        
    



print(find_mismatch("Python","Java"))


