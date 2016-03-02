from itertools import permutations
def sol3(s):
    l=["".join(i) for i in permutations(s,3)]
    for i in l:
        n=int(i)
        if n%8==0:
            return True
    return False
def sol2(s):
    l=["".join(i) for i in permutations(s)]
    for i in l:
        n=int(i)
        if n%8==0: return True
    return False
T=int(raw_input())
for t in range(T):
    s=str(raw_input())
    b=False
    if len(s)>2: b=sol3(s)
    else: b=sol2(s)
    if b: print "YES"
    else: print "NO"
        
