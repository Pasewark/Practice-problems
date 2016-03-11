class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def loop(l):
    nodes=set()
    current=l
    while current!=None:
        if current in nodes: return current
        nodes.add(current)
        current=current.nxt
    return False
