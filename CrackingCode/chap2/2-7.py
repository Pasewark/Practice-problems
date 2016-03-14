class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def intersect(l,m):
    nodes=set()
    current=l
    while current!=None:
        nodes.add(current)
        current=current.nxt
    current=m
    while current!=None:
        if current in nodes: return True
        current=current.nxt
    return False
