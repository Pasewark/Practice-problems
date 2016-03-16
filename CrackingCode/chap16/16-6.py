def diff(l,m):
    l=sorted(l)
    minimum=abs(l[0]-m[0])
    for i in m:
        lo=0
        hi=len(l)-1
        mid=0
        while hi>=lo:
            mid=(hi+lo)/2
            if l[mid]>i:
                hi=mid-1
            elif l[mid]<i:
                lo=mid+1
            else: return 0
        for ind in range(3):
            try:
                minimum=min(abs(l[ind-1]-i),minimum)
            except IndexError: continue
    return minimum
