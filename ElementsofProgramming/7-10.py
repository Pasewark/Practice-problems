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

def reverse(h):
    prev=None
    temp=None
    current=h
    while current!=None:
        temp=current.nxt
        current.nxt=prev
        prev=current
        current=temp
    return prev

def isPal(h):
    l=1
    current=h
    while current.nxt!=None:
        l+=1
        current=current.nxt
    start=l/2+l%2
    current=h
    while start>0:
        current=current.nxt
        start-=1
    h2=reverse(current)
    current=h
    current2=h2
    while current2!=None:
        if current.value!=current2.value: return False
        current=current.nxt
        current2=current2.nxt
    return True
