def charToNum(c):
    if c=='A': return 10
    if c=='B': return 11
    if c=='C': return 12
    if c=='D': return 13
    if c=='E': return 14
    if c=='F': return 15
    else: return int(c)
def digToChar(d):
    if d<10: return str(d)
    if d==10: return 'A'
    if d==11: return 'B'
    if d==12: return 'C'
    if d==13: return 'D'
    if d==14: return 'E'
    if d==15: return 'F'
def convertBase(s,a,b):
    if s=='0': return '0'
    n=0
    for i in s:
        n*=a
        n+=charToNum(i)
    t=''
    while n>0:
        t+=digToChar(n%b)
        n/=b
    return t[::-1]

