def parity(n):
    count=0
    num=1
    while num<=n:
        if n&num>0:
            count+=1
        num<<=1
    return count%2
