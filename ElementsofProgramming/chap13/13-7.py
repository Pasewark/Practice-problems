def chars(s):
    d={}
    for i in s:
        if i in d: d[i]+=1
        else: d[i]=1
    print sorted([(i,d[i]) for i in d],key=lambda (x,y): x)
