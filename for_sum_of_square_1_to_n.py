# Using a for loop, write a program which asks the user to type a positive integer, n, and
# then prints the sum of the square of all numbers form 1 to n (including both 1 and n).
# For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14
user_num=int(input("Enter your number "))
num=0
sq=0
total=0
for num in range(1,user_num+1):
    sq=num**2
    total=total+sq
print(total)

