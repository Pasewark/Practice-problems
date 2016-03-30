def intToString(n):
    if n==0: return '0'
    s=''
    while n>0:
        s+=str(n%10)
        n/=10
    return s[::-1]

def stringToInt(s):
    n=0
    for i in s:
        n*=10
        n+=int(i)
    return n

