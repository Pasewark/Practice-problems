def sv():
    n=2000
    l=range(n)
    l[1]=0
    for i in range(2,int(n**.5)+1):
        if l[i]: l[i*i:n-1:i]=[0]*len(xrange(i*i,n-1,i))
    return filter(None,l)
def sol(n,l):
    ba=-n
    bb=-n
    c=0
    for a in range(-n,n+1):
        for b in range(-n,n+1):
            i=0
            while i**2+a*i+b in l:
                i+=1
            if i>c:
                #print a,b
                c=i
                ba=a
                bb=b
    return [ba,bb]
                
l=sv()
n=int(raw_input())
print " ".join(map(str,sol(n,set(l))))
