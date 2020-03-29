#Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.
num=0
total=0
for num in range(1,102):
    if num%2==0:
        total=total+num
print(total)
