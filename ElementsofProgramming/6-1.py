def swap(l,i,j):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
def part(l,m):
    i=0
    j=0
    n=len(l)-1
    while j<=n:
        if l[j]<m:
            swap(l,i,j)
            i+=1
            j+=1
        elif l[j]>m:
            swap(l,j,n)
            n-=1
        else: j+=1
