from collections import defaultdict
def sol(s,edges,n):
    visited,q={},[s]
    for i in range(n):
        visited[i+1]=-1
    visited[s]=0
    while q:
        current=q.pop(0)
        for v in edges[current]:
            if visited[v]==-1:
                visited[v]=visited[current]+1
                q.append(v)
    visited[s]=-2
    return visited

T=int(raw_input())
sols=[]
for t in range(T):
    edges=defaultdict(list)
    N,M=map(int,raw_input().split())
    for m in range(M):
        a,b=map(int,raw_input().split())
        edges[a].append(b)
        edges[b].append(a)
    s=int(raw_input())
    sols.append(sol(s,edges,N))
for i in sols:
    for j in range(len(i.keys())):
        if i[j+1]==-1: print -1,
        elif i[j+1]==-2: continue
        else: print i[j+1]*6,
    print ""
