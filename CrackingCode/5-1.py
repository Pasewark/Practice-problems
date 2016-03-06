def solve(n,m,i,j):
    n=clear(n,i,j)
    m<<=i
    return n|m

def clear(n,i,j):
    c=1<<(j-i+1)
    c-=1
    c<<=i
    n&=~c
    return n
