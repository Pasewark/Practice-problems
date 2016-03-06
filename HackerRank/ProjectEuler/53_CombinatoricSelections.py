N,K=map(int,raw_input().split())
combs=[[1]]
tot=0
for n in range(2,N+2):
    ls=[]
    for r in range(n):
        if r==0:app=1
        elif r==n-1:app=1
        else:
            app=combs[-1][r]+combs[-1][r-1]
        ls.append(app)
        if app>K:tot+=1
    combs.append(list(ls))
print tot
