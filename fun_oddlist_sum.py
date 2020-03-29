#Write a function that accepts a list of integers as parameter.
#Your function should return the sum of all the odd numbers in the list.
#If there are no odd numbers in the list,
#your function should return 0 as the sum.
def sum_oddlist(mylist):
    sum=0
    for item in mylist:
        if item%2!=0:
            sum=sum+item
    return sum

        
