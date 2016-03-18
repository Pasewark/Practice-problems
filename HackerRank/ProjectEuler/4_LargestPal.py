ls=[]
def check(l):
    for i in range(len(l)/2):
        if l[i]!=l[-i-1]: return False
    return True
def start():
    for i in range(100,999):
        for j in range(i,999):
            m=i*j
            if m<1000000 and m>100000 and check(map(int,list(str(m)))):
                ls.append(m)
    ls.sort()
def sol(n):
    M=0
    for i in ls:
        if i>n: return M
        M=i


T=int(raw_input())
sols=[]
start()
for t in range(T):
    sols.append(sol(int(raw_input())))
for i in sols: print i
