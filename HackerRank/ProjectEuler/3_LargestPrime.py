def sol(n):
    pf=2
    largest=1
    while pf*pf<=n:
        while n%pf==0:
            largest=pf
            n/=pf
        pf+=1
    if n>1: return n
    return largest

T=int(raw_input())
sols=[]
for t in range(T):
    sols.append(sol(int(raw_input())))
for i in sols: print i
