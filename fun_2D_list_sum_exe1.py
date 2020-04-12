# Write a function which accepts a 2D list of numbers and returns the sum of 
# all the number in the list You can assume that the number of columns in 
# each row is the same
def mf_list_sum(mylist):
    list_sum=0
    for i in mylist:
        for j in range(0,len(i)):
            list_sum+=i[j]
    return list_sum

print("Sun : ",mf_list_sum([[89,87,88],[91,92,87],[89,90,87]]))