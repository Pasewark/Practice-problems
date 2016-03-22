def solve(n):
    i=2
    tot=0
    rn=int(round(n**.5))
    while i<rn+1:
        if (n/i)*i==n:
            if i%2==0: tot+=1
            if (n/i)%2==0 and n/i!=i: tot+=1
        i+=1
    if n%2==0: tot+=1
    return tot

T=int(raw_input())
for t in range(T):
    print solve(int(raw_input()))
