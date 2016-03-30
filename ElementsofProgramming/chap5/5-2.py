def swap(n,i,j):
    ni=0
    if n&(1<<i)>0: ni=1
    nj=0
    if n&(1<<j)>0: nj=1
    if ni>0:
        n|=(1<<j)
    else: n&=(~(1<<j))
    if nj>0:
        n|=(1<<i)
    else: n&=(~(1<<i))
    return n
