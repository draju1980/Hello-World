def loan_py_mnt(pa,rate,dur):
    if rate==0:
        mnt_py=pa/dur*12
        return mnt_py
    r=rate/100/12
    n=dur*12
    mnt_py=pa*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    return mnt_py
print(loan_py_mnt(1000.0,4.5,5))



    
