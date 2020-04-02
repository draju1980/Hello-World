# Encryption problem: You and your friend want to encrypt your messages and
# you have shared a secret key that is known to just the two of you. Every
# character in the character_set is mapped to some other character in the
# secret key. For example 'a' is mapped to 'D', 'b' is mapped to 'd', 'c' is
# mapped to '1' and so forth as shown below:

# character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
# secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

# Write a function named my_encryption that accepts a string
# (a message which will only consist of the characters from the character set)
# as function parameter and encrypts that message using the secret_key and
# returns it. For example if input to this function (the message that you
# want to send) is:

def _encryption_sample_ed2_0215(my_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted_message = ""
    for character in my_string:
        index = character_set.find(character)
        encrypted_message = encrypted_message + secret_key[index] 
  
    return encrypted_message
