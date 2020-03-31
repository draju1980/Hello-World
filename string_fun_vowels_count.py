# Write a function which returns the total number of vowels in an input string
# which consists of alphabetic characters. Note that capitalization does not
# matter here i.e. a lower case character should be considered the same as an
# upper case character. For this problem, the vowels are considered to
# be A, E, I, O, U.
def vowels_count(x):
    count=0
    for word in x:
        if word=="a" or word=="A" or word=="e" or word=="E" or word=="i" or word=="I" or word=="o" or word=="O" or word=="u" or word=="U":
            count=count+1
    return count

print(vowels_count("hello"))
