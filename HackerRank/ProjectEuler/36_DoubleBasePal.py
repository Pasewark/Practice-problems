def ispal(s):
    for j in range(len(s)/2):
        if s[j]!=s[-j-1]: return False
    return True
def base(n,k):
    s=''
    while n>0:
        s=str(n%k)+s
        n/=k
    return s
def sol(n,k):
    s=0
    for i in range(n):
        if not ispal(str(i)): continue
        if ispal(base(i,k)): s+=i
    return s
n,k=map(int,raw_input().split())
print sol(n,k)
