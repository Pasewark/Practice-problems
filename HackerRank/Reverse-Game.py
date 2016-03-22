T=int(raw_input())
for t in range(T):
    n,k=map(int,raw_input().split())
    if k<n/2: print k*2+1
    else: print (n-k-1)*2
