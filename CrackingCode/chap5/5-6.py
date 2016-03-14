def change(n,m):
    k=n^m
    i=0
    total=0
    while (1<<i)<=k:
        if (1<<i)&k>0: total+=1
        i+=1
    return total
