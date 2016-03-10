def search(A,b):
    A.extend(A)
    lo=0
    hi=len(A)-1
    lower=True
    mid=(lo+hi)/2
    if A[mid]<b:
        lo=mid+1
        lower=False
    elif A[mid]>b:
        hi=mid-1
        lower=True
    else: return mid
    while lo<=hi:
        mid=(lo+hi)/2
        if A[mid]<b:
            if lower:
                lo=mid+1
                lower=False
            else:
                hi=mid-1
                lower=True
        elif A[mid]>b:
            if lower:
                lo=mid+1
                lower=True
            else:
                hi=mid-1
                lower=False
        else:
            if mid>len(A)/2: return mid-len(A)/2
            return mid
    return -1
