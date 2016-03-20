def findSum(l,a):
    d={}
    for i in l:
        if i in d: d[i]+=1
        else: d[i]=1
    sols=[]
    for i in l:
        if a-i in d:
            if a-i==i and d[i]==1:continue
            else: sols.append((a-i,i))
    return sols
