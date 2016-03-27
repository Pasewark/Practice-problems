class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        print self.value
        current=self
        while current.nxt!=None:
            current=current.nxt
            print current.value

def cycle(L):
    current=L
    nodes=set()
    nodes.add(current)
    while current.nxt!=None:
        current=current.nxt
        if current in nodes:
            return current
        nodes.add(current)
    return -1

