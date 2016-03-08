def primes(n):
    n1=n+1
    primes=range(n1)
    primes[1]=0
    sqrtn=int(round(n**.5))
    for i in range(2,sqrtn+1):
        if primes[i]: primes[i*i:n1:i]=[0]*len(xrange(i*i,n1,i))
    return filter(None,primes)
