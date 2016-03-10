def closest(l):
    m=len(l)
    d={}
    for i in range(len(l)):
        if l[i] in d:
            m=min(m,i-d[l[i]])
        d[l[i]]=i
    if m<len(l): return m
    return -1

