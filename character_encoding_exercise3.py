# Write a function that accepts an alphabetic string and returns an integer
# which is the sum of all the UTF-8 codes of the character in that string.

def _sum_of_haracters_(a):
    total=0
    for i in a:
        total = total + ord(i)
    return total
    
print(_sum_of_haracters_("hello"))
