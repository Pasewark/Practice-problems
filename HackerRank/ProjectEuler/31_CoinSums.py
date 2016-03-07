def gen(n):
    ls=[0 for i in range(n)]
    ls[0]=1
    for i in [1,2,5,10,20,50,100,200]:
        for j in range(len(ls)):
            if j-i>-1:ls[j]=ls[j]+ls[j-i]
    return ls
ls=gen(10**5+1)
def sol(n):
    return ls[n]%(10**9+7)

T=int(raw_input())
sols=[]
for t in range(T):
    sols.append(sol(int(raw_input())))
for i in sols: print i
