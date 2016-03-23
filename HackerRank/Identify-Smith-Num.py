def factor(n):
    factors=[]
    pf=2
    while pf*pf<=n:
        while n%pf==0:
            factors.append(pf)
            n/=pf
        pf+=1
    if n>1: factors.append(n)
    return factors
n=raw_input()
if sum(map(int,list("".join(map(str,factor(int(n)))))))==sum(map(int,list(n))): print 1
else: print 0
