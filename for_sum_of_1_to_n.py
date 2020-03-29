#Using a for loop, write a program which asks the user to type an integer, n,
#and then prints the sum of all numbers from 1 to n (including both 1 and n

user_num=int(input("Enter your number "))
num=0
total=0
for num in range(1,user_num+1):
        total=total+num
print(total)