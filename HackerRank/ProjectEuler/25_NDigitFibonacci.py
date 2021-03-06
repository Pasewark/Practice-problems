import math
import decimal
root5=decimal.Decimal(5).sqrt()
phi=(root5-1)/2
Phi=(root5+1)/2
def fib(n):
    return (Phi**n+phi**n)/root5
        
def sol1(n):
    return int(round(-1*(((n-1.0)+math.log10(5.0)/2.0)/(math.log10(phi)))))+1
def sol2(n):
    n=decimal.Decimal(n-1)
    return int(round(-1*((n+decimal.Decimal(5).log10()/decimal.Decimal(2.0))/(phi.log10()))))+1
def sol(n):
    if n==1: return 1
    if n==0: return 0
    current=sol2(n)
    p=decimal.Decimal(10**(n-1))
    while fib(current)>p:
        current-=1
    return current+1
    
T=int(raw_input())
sols=[]
for t in range(T):
    sols.append(sol(int(raw_input())))
for i in sols: print i
    
