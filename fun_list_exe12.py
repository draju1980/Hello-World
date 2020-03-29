# Write a program that asks the user to enter an integer between 1 and 9999
# (both inclusive) and then prints the input integer using words. For example
# if the user enters:
# 3421
# Then your program should print
# three thousand four hundred twenty one
n=int(input("Enter an integer between 1 and 9999 "))
one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_to_ninety=['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']
temp_str=""
if n==0:
    temp_str='zero'
    #print('zero')
first_digit=n//1000
second_digit=(n%1000)//100
third_digit=(n%100)//10
fourth_digit=(n%10)
if first_digit>0:
    temp_str=temp_str+one_to_ten[first_digit]+' thousand '
    #print (one_to_ten[first_digit],'thousand ',end='')
if second_digit>0:
    temp_str=temp_str+one_to_ten[second_digit]+' hundred '
    #print (one_to_ten[second_digit],'hundred ',end='')
if third_digit>1:
    temp_str=temp_str+twenty_to_ninety[third_digit]+" "
    #print (twenty_to_ninety[third_digit],'',end='')
if third_digit==1:
    temp_str=temp_str+ten_to_nineteen[fourth_digit]+" "
    #print (ten_to_nineteen[fourth_digit],'',end='')
else:
    if fourth_digit:
        temp_str=temp_str+one_to_ten[fourth_digit]+" "
        #print (one_to_ten[fourth_digit],'',end='')
if temp_str[-1]==" ":
    temp_str=temp_str[0:-1]
print (temp_str)
