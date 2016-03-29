def pal(s):
    d={}
    for i in s:
        if i in d: d[i]+=1
        else: d[i]=1
    return sum([d[i]%2 for i in d])<2
