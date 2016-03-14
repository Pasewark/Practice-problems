def find(l):
    hi=len(l)-1
    lo=0
    while hi>=lo:
        mid=(hi+lo)/2
        if l[mid]>mid: hi=mid-1
        elif l[mid]<mid: lo=mid+1
        else: return mid
    return -1
