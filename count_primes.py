# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶

# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.

def count_primes(num):
  pcount=[]
  for i in range(1,num):
    if num%i==0:
      continue      
    else:
      pcount.append(i)
  return len(pcount)
print(count_primes(100))
