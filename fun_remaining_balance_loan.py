def loan_balance(pa,rate,dur,py):
    if rate==0:
        return pa-py*(pa/(dur*12.0))
    r=rate/100/12.0
    n=dur*12
    loan_balance=pa*((1.0+r)**n-(1.0+r)**py)/(((1.0+r)**n)-1)
    return loan_balance
)
