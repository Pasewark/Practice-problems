n=int(raw_input())
def solve(l):
    if len(l)==1: return 0
    else: return reduce(lambda x,y:x*y,l,1)%1234567
for i in range(n):
    m=int(raw_input())
    nums=map(int,raw_input().split())
    print solve(nums)
