# Write a program using while loops that asks the user for a positive
# integer 'n' and prints a triangle using numbers from 1 to 'n'.

n=int(input("Enter the number "))
for i in range(1,n+1):
    print(str(i)*i)
