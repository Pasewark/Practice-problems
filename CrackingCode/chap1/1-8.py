def zero(m):
    inds=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==0:inds.append((i,j))
    for ind in inds:
        for i in range(len(m)):
            m[i][ind[1]]=0
        for j in range(len(m[0])):
            m[ind[0]][j]=0
    return m
