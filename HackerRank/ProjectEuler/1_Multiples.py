def s(n): return n*(n+1)/2
T=int(raw_input())
sols=[]
for t in range(T):
    n=int(raw_input())-1
    sols.append(s(n/3)*3+s(n/5)*5-s(n/15)*15)
for i in sols: print i
