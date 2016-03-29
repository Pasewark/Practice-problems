def possible(l,m):
    d={}
    for i in m:
        if i in d: d[i]+=1
        else: d[i]=1
    for i in l:
        if i in d:
            d[i]-=1
            if d[i]<0: return False
        else: return False
    return True
