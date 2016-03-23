def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
T=int(raw_input())
for t in range(T):
    n=int(raw_input())
    if reduce(lambda x,y:gcd(x,y),map(int,raw_input().split()))==1: print "YES"
    else: print "NO"
