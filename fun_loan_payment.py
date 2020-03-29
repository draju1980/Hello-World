#Write a function that calculates and returns the monthly payments for a loan.
#This function accepts three parameters in the exact order (principal, annual_interest_rate, duration):

#principal: The total amount of loan. Assume that the principal is a positive floating point number.

#annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
#duration: number of years to pay the loan back. Assume that duration is a positive integer.
#To calculate the amount of monthly payment for the loan you should use the following equation

#MonthlyPayment=Principal∗r(1+r)n/(1+r)n−1 
#   Where:

#r is the monthly interest rate (should be calculated by first dividing the annual_interest_rate by 100
# and then divide the result by 12 to make it monthly). Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation: MonthlyPayment=Principaln 

# n is the total number of monthly payments for the entire duration of the loan (Notice that n is equal to loan duration in years multiplied by 12).

def loan_payment(pa,rate,dur):
    if rate==0:
        return pa/(dur*12)
    r=rate/100/12
    n=dur/12
    mpay=pa*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return mpay
