def sol(n):
    s1=1
    s2=2
    s=0
    while s2<=n:
        if s2%2==0: s+=s2
        temp=s2
        s2=s1+s2
        s1=temp
    return s

T=int(raw_input())
sols=[]
for t in range(T):
    sols.append(sol(int(raw_input())))
for i in sols: print i
