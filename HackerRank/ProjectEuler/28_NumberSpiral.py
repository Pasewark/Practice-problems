def s1(n):
    return n*(n+1)/2
def s2(n):
    return n*(n+1)*(2*n+1)/6
def sd1(n):
    return 4*s2(n)-4*s1(n)+n
def sol(n):
    d1=sd1(n)
    d2=d1-2*s1(n-1)
    d3=d2-2*s1(n-1)
    d4=d3-2*s1(n-1)
    return (d1+d2+d3+d4-3)%(10**9+7)

T=int(raw_input())
sols=[]
for t in range(T):
    sols.append(sol(int(raw_input())/2+1))
for i in sols: print i
