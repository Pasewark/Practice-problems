class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def find(L,k):
    num=0
    current=L
    while current!=None:
        num+=1
        current=current.nxt
    current=L
    while num!=k:
        num-=1
        current=current.nxt
    return current.value
