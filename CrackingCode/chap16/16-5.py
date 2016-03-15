def count(n):
    i=1
    tot=0
    while n/5**i>0:
        tot+=n/5**i
        i+=1
    return tot

