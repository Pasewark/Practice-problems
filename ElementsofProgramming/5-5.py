def powerSet(s):
    num=0
    while num<2**len(s):
        bnum=bin(num)[-1:1:-1]
        output=[]
        for i in range(len(bnum)):
            if bnum[i]=='1': output.append(s[i])
        if len(output)==0: print '{emptyset}'
        else: print ",".join(map(str,output))
        num+=1

powerSet([1,2,3,4])
