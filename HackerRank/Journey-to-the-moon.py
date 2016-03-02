from collections import defaultdict
N,l = map(int,raw_input().split())
d=defaultdict(set)
for i in xrange(l):
    a,b = map(int,raw_input().split())
    d[a].add(b)
    d[a].add(a)
    d[a].update(d[b])
    for n in d[b]:
        d[n]=d[a]
    d[b]=d[a]
l=[]
superset=set()
somenum=0
for k in range(N):
    if len(d[k])==0:
        l.append(1)
    else:superset.add(frozenset(d[k]))

tempset=set()
for el in superset:
    l.append(len(el))
    tempset.update(el)
sumdict={}
currentsum=0
sumdict[len(l)]=0
for i in range(len(l)-1,-1,-1):
    currentsum+=l[i]
    sumdict[i]=currentsum
sm=0
for i in range(len(l)):
    sm+=l[i]*sumdict[i+1]
print sm
