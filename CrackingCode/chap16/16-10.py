def year(l):
    totals=[0 for i in range(2000)]
    for i in l:
        totals[i[0]]+=1
        totals[i[1]+1]-=1
    total=0
    M=0
    Myear=0
    for i in range(len(totals)):
        total+=totals[i]
        if total>M:
            M=total
            Myear=i
    return Myear
