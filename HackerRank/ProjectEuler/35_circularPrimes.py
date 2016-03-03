def pf(n):
    np1=n+1
    s=range(np1)
    s[1]=0
    sqrtn=int(round(n**.5))
    for i in range(2,sqrtn+1):
        if s[i]: s[i*i:np1:i]=[0]*len(xrange(i*i,np1,i))
    return filter(None,s)
prms=pf(10**6)
prmset=set(prms)
def iscprm(n):
    s=str(n)
    s2=s
    for i in range(len(s)-1):
        s2=s2[1:]+s2[0]
        if int(s2) not in prmset: return False
    return True
n=int(raw_input())
sm=0
for i in prms:
    if i>=n: break
    if iscprm(i): 
        sm+=i
print sm
