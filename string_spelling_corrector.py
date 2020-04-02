# Write a function named spelling_corrector that accepts two arguments. The
# first argument is a sentence (string) and the second argument is a list of
# words (correct_spells). Your function should check each word in the input
# string against all the words in the correct_spells list and return a string
# such that:

# If a word in the original sentence matches exactly with a word in the
# correct_spells then the word is not modified and it should be directly
# copied to the output string.

# if a word in the sentence can match a word in the correct_spells list by
# replacing, inserting, or deleting a single character, then that word should
# be replaced by the correct word in the correct_spelled list.

# If neither of the two previous conditions is true, then the word in the
# original string should not be modified and should be directly copied to the
# output string.
################### Instructor function ###################
def _instructor_function (s,correct_spelled):
    words=s.strip().split()
    output_str=""
    for current_word in words:
        if len(current_word)<=2 or (current_word in correct_spelled) :
            output_str=output_str+" "+current_word
            continue
        min_mismatch=2
        replacement_word=current_word
        for correct_word in correct_spelled:
            if min(_find_mismatch(current_word,correct_word), _single_insert_or_delete(current_word,correct_word))==1:
                replacement_word=correct_word
                break
        output_str=output_str+" "+replacement_word
    return output_str.strip().lower()
def _find_mismatch(s1,s2):
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
def _single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
