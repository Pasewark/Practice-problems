def b(sols,l1,l2,i,j):
    if i==0 or j==0: return []
    elif l1[i-1]==l2[j-1]: return b(sols,l1,l2,i-1,j-1)+[l1[i-1]]
    else:
        if sols[i][j-1]>sols[i-1][j]: return b(sols,l1,l2,i,j-1)
        else: return b(sols,l1,l2,i-1,j)

def sol(l1,l2):
    sols=[[0 for j in range(len(l2)+1)] for i in range(len(l1)+1)]
    for i in range(1,len(l1)+1):
        for j in range(1,len(l2)+1):
            if l1[i-1]==l2[j-1]: sols[i][j]=sols[i-1][j-1]+1
            else: sols[i][j]=max(sols[i][j-1],sols[i-1][j])
    return b(sols,l1,l2,len(l1),len(l2))

n,m=map(int,raw_input().split())
l1=map(int,raw_input().split())
l2=map(int,raw_input().split())
print " ".join(map(str,sol(l1,l2)))
