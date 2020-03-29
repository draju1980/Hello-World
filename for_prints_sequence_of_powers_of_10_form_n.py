# Write a program that asks the user for an input 'n'(assume that the user enters a positive integer) 
# and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines.
# For example if 'n' is equal to 4 then the output should look like the following
#1
#10
#100
#1000
#10000
user_num=int(input("enter the number "))
num=0
sq=0
for num in range(0,user_num+1):
    sq=10**num
    print(sq)
    
    
