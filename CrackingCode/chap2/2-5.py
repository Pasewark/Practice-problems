class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def sm(l,m):
    lnum=0
    mnum=0
    current=l
    ten=0
    while current!=None:
        lnum+=current.value*(10**ten)
        current=current.nxt
        ten+=1
    current=m
    ten=0
    while current!=None:
        mnum+=current.value*(10**ten)
        current=current.nxt
        ten+=1
    num=mnum+lnum
    n=node(num%10)
    num/=10
    current=n
    while num>0:
        current.nxt=node(num%10)
        current=current.nxt
        num/=10
    return n
