import math
def sol(s,n):
    if s=='': return ''
    l=len(s)
    i=0
    while math.factorial(l-1)<=n:
        i+=1
        n-=math.factorial(l-1)
    return s[i]+sol(s[:i]+s[i+1:],n)

T=int(raw_input())
sols=[]
for t in range(T):
    sols.append(sol('abcdefghijklm',int(raw_input())-1))
for i in sols: print i
