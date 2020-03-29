#Write a function that accepts a list of integers and returns the average.
#Assume that the input list contains only numbers. 
def list_avg(mylist):
    sum=0
    for item in mylist:
        sum=sum+int(item)
    result=(sum/len(mylist))
    return result
