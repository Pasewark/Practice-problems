from collections import defaultdict
def ispal(s):
    for i in range(len(s)/2):
        if s[i]!=s[-i-1]: return False
    return True
def it(s,i):
    if ispal(s): return s
    if i>59: return str(-1)
    s=int(s)+int(s[::-1])
    return it(str(s),i+1)
def sol(n):
    dic=defaultdict(int)
    M=0
    Mpal=-1
    for ind in range(n+1):
        st=it(str(ind),0)
        num=int(st)
        if num==-1: continue
        dic[num]+=1
        if dic[num]>M:
            M=dic[num]
            Mpal=num
    print Mpal,M
n=int(raw_input())
sol(n)
