def find(l):
    current=l[0]
    largest=l[0]
    for i in l[1:]:
        current+=i
        current=max(current,0)
        largest=max(current,largest)
    if largest>0: return largest
    return 0
