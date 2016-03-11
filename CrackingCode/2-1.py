class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def dup(l):
    nodes=set()
    current=l
    nodes.add(current.value)
    while current.nxt!=None:
        if current.nxt.value in nodes:
            current.nxt=current.nxt.nxt
            continue
        nodes.add(current.nxt.value)
        current=current.nxt
