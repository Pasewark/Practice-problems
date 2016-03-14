def maxOnes(n):
    l=map(int,list(bin(n)[2:]))
    lastInd=0
    current=0
    for i in range(len(l)):
        if l[i]==0:
            l[lastInd]+=current
            l[i]=current
            current=0
            lastInd=i
        if l[i]==1:
            current+=1
    if current==len(l): return current
    return max(l)
