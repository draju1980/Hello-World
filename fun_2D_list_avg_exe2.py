# Write a function that accepts a 2 Dimensional list of integers and 
# returns the average. 
# Remember that average = (sum_of_all_items) / (total_number_of_items).
def mf_list_sum(mylist):
    total=0
    index=0
    for row in range(len(mylist)):
        for col in range(len(mylist[row])):
                         total=total+mylist[row][col]
                         index=index+1
    return total/index

print("Avrage : ",mf_list_sum([[2, 2, 2, 2], [2, 2, 2, 2]]))