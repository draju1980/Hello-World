# Write a function called pattern_sum that receives two single digit positive
# integers, (k and m) as parameters and calculates and returns the total
# sum as:
# k + kk + kkk + .... (the last number in the sequence should have m digits)
def pattern_sum(a, b):
    psum=[]
    total=0
    for i in range(1,b+1):
        psum.insert(i,str(a)*i)
    for item in psum:
        total=total+int(item)
    return total
    


print(pattern_sum(5,3))

