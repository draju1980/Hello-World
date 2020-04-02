#Write a function named count_consonants that receives a string as parameter
# and returns the total count of the consonants in the string. Consonants are
# all the characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'.
# If the same consonant repeats multiple times you should count all of them.
# Note that capitalization and punctuation does not matter here i.e. a lower
# case character should be considered the same as an upper case character.

################### Instructor function ###################
def _total_consonants_sample_(sample_string):
    spaces_removed = sample_string.replace(" ", "")
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in spaces_removed.lower():
        if char not in vowels:
            count = count + 1
    return count

 
