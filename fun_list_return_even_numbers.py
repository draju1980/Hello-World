# Write a function which accepts an input list of numbers and returns a list which includes
# only the even numbers in the input list. If there are no even numbers in the
# input numbers then your function should return an empty list.
def list_even(mylist):
    even=[]
    for item in mylist:
        if (item%2)==0:
            even.append(item)
    return even
print(list_even([3, 4, -6, 1, 0]))
