N=int(raw_input())
num=3
de=2
for i in range(N):
    if len(str(num))>len(str(de)):
        print i+1
    c=num+de
    num=c+de
    de=c
