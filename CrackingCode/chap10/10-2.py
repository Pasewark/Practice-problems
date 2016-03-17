def group(A):
    d={}
    l=[]
    for s in A:
        key="".join(sorted([c for c in s]))
        if key in d:
            d[key].append(s)
        else: d[key]=[s]
    for key in d:
        l.extend(d[key])
    return l
