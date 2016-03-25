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
