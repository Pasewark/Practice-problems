M={}
primes=[]
def sv():
    s=range(217288)
    s[1]=0
    sqrtn=int(round(217288**.5))
    for i in range(2,sqrtn+1):
        if s[i]: s[i*i: 217287: i]=[0]*len(xrange(i*i,217287,i))
    return filter(None,s)
def pl(n):
    j=0
    while primes[j]<=n:
        j+=1
    return j

def sol(n):
    if n in M: return M[n]
    if n<0: return 0
    if n==0: return 1
    M[n]=sol(n-1)+sol(n-4)
    return M[n]

T=int(raw_input())
sols=[]
primes=sv()
for t in range(T):
    sols.append(sol(int(raw_input())))
for i in sols: print pl(i)
