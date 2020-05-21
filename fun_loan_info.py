# Your function for calculating payment goes here
def loan_py_mnt(pa,rate,dur):
    if rate==0:
        mnt_py=pa/dur*12
        return mnt_py
    r=rate/100/12
    n=dur*12
    mnt_py=pa*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return mnt_py

# Your function for calculating remaining balance goes here
def loan_balance(pa,rate,dur,py):
    if rate==0:
        return pa-py*(pa/(dur*12.0))
    r=rate/100/12.0
    n=dur*12
    loan_balance=pa*((1.0+r)**n-(1.0+r)**py)/(((1.0+r)**n)-1)
    return loan_balance

# Your main program goes here
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
monthly_payment=loan_py_mnt(principal,annual_interest_rate,duration)
print("LOAN AMOUNT:",principal,"INTEREST RATE (PERCENT):",annual_interest_rate)
print("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(monthly_payment))
for year in range(1,1+duration):
    balance=loan_balance(principal,annual_interest_rate,duration,year*12)
    print("YEAR:",year,"BALANCE:",int(balance),"TOTAL PAYMENT ",int(monthly_payment*year*12))