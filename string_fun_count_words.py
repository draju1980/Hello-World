# Write a function that accepts a string and a character as input and returns
# the count of all the words in the string which start with the given character.
# Assume that capitalization does not matter here. You can assume that the input
# string is a sentence i.e. words are separated by spaces and consists of
# alphabetic characters.
def word_count(input_string,word):
    my_count = 0
    word=word.lower()
    string_list=input_string.lower().split()
    # Iterate through each character in the given string
    # and check if the input character is equal to the
    # character in the string. If it does increase the
    # count by 1 and finally return the count
    for character in string_list:
        if character[0] == word:
            my_count = my_count + 1
    return my_count

print(word_count("Hello World","l"))
    
