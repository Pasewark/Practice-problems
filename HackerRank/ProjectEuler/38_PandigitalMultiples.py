def sol(n,k):
    s=''
    if k==8: s='12345678'
    else: s='123456789'
    nums=[]
    for i in range(2,n):
        numbers=set(s)
        add=True
        for j in xrange(1,n):
            if not add: break
            if len(numbers)==0:
                nums.append(i)
                break
            current=str(j*i)
            for letter in current:
                if letter in numbers:
                    numbers.remove(letter)
                else: 
                    add=False
                    break
    return nums
            

n,k=map(int,raw_input().split())
for i in sol(n,k): print i
