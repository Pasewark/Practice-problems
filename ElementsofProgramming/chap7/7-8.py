class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        print current.value
        while current.nxt!=None:
            current=current.nxt
            print current.value

def find(h,k):
    current=h
    currentk=h
    while k>0:
        currentk=currentk.nxt
        k-=1
    while currentk!=None:
        current=current.nxt
        currentk=currentk.nxt
    return current
