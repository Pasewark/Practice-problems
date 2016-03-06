N,K=map(int,raw_input().split())
sols=[]
for i in range(1,N+1):
    isperm=True
    tempsol=[str(i)]
    for j in range(K-1):
        tempsol.append(str(i*(j+2)))
        if sorted(str(i))!=sorted(str(i*(j+2))):
            isperm=False
            break
    if isperm: sols.append(list(tempsol))
for i in sols:
    print " ".join(i)
