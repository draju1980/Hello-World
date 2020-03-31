# Write a function that takes a string consisting of alphabetic characters
# as input argument and returns True if the string is a palindrome. A
# palindrome is a string which is the same backward or forward. Note that
# capitalization does not matter here i.e. a lower case character can be
# considered the same as an upper case character.
def _is_palindrome_sample_(sample_string):
    # Check if the inverted string  equals the original string
    if str(sample_string).lower() == str(sample_string)[::-1].lower():
        return True     # Sample string is a palindrome
    else:
        return False    # Sample string is not a palindrome
    
    
    
print(_is_palindrome_sample_('macbook'))

