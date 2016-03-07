import math
n=int(raw_input())
s=0
for i in range(19,n):
    s2=sum(math.factorial(int(num)) for num in str(i))
    if s2%i==0: s+=i
print s
