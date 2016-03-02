visited=set()
def dfs(mat,p):
    cvisited,stack=set(),[p]
    while stack:
        point=stack.pop()
        if point not in cvisited:
            cvisited.add(point)
            visited.add(point)
            for i in range(3):
                for j in range(3):
                    if mat[point[0]+i-1][point[1]+j-1]==1 and (point[0]+i-1,point[1]+j-1) not in cvisited: stack.append((point[0]+i-1,point[1]+j-1))
    return len(cvisited)
    
M=int(raw_input())
N=int(raw_input())
mat=[]
mat.append([0 for i in range(N+2)])
for m in range(M):
    mat.append([0]+(map(int,raw_input().split()))+[0])
mat.append([0 for i in range(N+2)])
maximum=0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if (i,j) not in visited and mat[i][j]==1:
            maximum=max(maximum,dfs(mat,(i,j)))
print maximum
