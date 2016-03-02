def fun(l,num):
    num%=len(l)
    l=l[num:]+l[:num]
    return l
        

m,n,r=map(int,raw_input().split())
mat=[]
for i in range(m):
    mat.append(map(int,raw_input().split()))
numrot=min(m,n)/2
lists=[]
for i in range(numrot):
    l=[]
    for j in range(i+1,n-i):
        l.append(mat[i][j])
    for j in range(1+i,m-i):
        l.append(mat[j][-i-1])
    for j in range(n-2-i,-1+i,-1):
        l.append(mat[-i-1][j])
    for j in range(m-2-i,-1+i,-1):
        l.append(mat[j][i])
    lists.append(l)
for i in range(len(lists)):
    lists[i]=fun(lists[i],r)
for i in range(len(lists)):
    for j in range(i+1,n-i):
        mat[i][j]=lists[i][j-i-1]
    for j in range(1+i,m-i):
        mat[j][-i-1]=lists[i][j-i-1+n-1-i*2]
    for j in range(n-2-i,-1+i,-1):
        mat[-i-1][j]=lists[i][n-2-i-j+n-1-i*2+m-1-i*2]
    for j in range(m-2-i,-1+i,-1):
        mat[j][i]=lists[i][m-2-i-j+n-1-i*2+m-1-i*2+n-1-i*2]
for ma in mat:
    for el in ma: print el,
    print
