def pf(n):
    np1=n+1
    s=range(np1)
    s[1]=0
    sqrtn=int(round(n**.5))
    for i in range(2,sqrtn+1):
        if s[i]: s[i*i:np1:i]=[0]*len(xrange(i*i,np1,i))
    return filter(None,s)
prms=pf(10**6)
def isperm(a,b):
    d={}
    for i in str(a):
        if i not in d:d[i]=1
        else: d[i]+=1
    for i in str(b):
        if d[i]==0: return False
        d[i]-=1
    return True
def gen(n):
    dic={}
    for i in prms:
        a=(frozenset(str(i)),len(str(i)))
        if a not in dic: dic[a]=[i]
        else: dic[a].append(i)
    return dic
dic=gen(10**6)
def find3(ls):
    st=set(ls)
    solist=[]
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if (ls[j]*2-ls[i]) in st: solist.append(long(str(ls[i])+str(ls[j])+str(ls[j]*2-ls[i])))
    return solist
def find4(ls):
    st=set(ls)
    solist=[]
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if (ls[j]*2-ls[i]) in st and (ls[j]+2*(ls[j]-ls[i])) in st:
                solist.append(long(str(ls[i])+str(ls[j])+str(ls[j]*2-ls[i])+str(ls[j]+2*(ls[j]-ls[i]))))
    return solist
def sol(n,k):
    sols=[]
    if k==3:
        for i in dic:
            sols.extend(find3(dic[i]))
    else:
        for i in dic:
            sols.extend(find4(dic[i]))
    return sorted(sols)
N,K=map(int,raw_input().split())
sls=sol(N,K)
#l=len(str(N))
for i in sls:
    s=str(i)
    l=len(str(i))/K
    if int(s[:l])<N:
        isp=True
        for k in range(K-1):
            if not isperm(s[l*k:l*(k+1)],s[l*(k+1):l*(k+2)]):isp=False
        if isp:print i
        
