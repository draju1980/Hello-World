# Write a function named find_gcd that accepts a list of positive integers
# and returns their greatest common divisor (GCD). Your function should
# return 1 as the GCD

def find_gcd(x):
    r=[]
    for i in range(1,len(x)+1):
        if int(x[i])%i==0:
            r.append(x(i))
    
    return r
print(find_gcd([13, 5, 9, 11, 3]))
