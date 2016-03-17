def merge(A,B):
    l=[]
    i=0
    j=0
    while True:
        if A[i]<B[j]:
            l.append(A[i])
            i+=1
            if i==len(A):
                l.extend(B[j:])
                return l
        else:
            l.append(B[j])
            j+=1
            if j==len(B):
                l.extend(A[i:])
                return l
