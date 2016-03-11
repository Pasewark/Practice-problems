class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt
            
#delete node at position i, where i is not the first or last node, w/o access to previous nodes
def delete(l):
    l.value=l.nxt.value
    l.nxt=l.nxt.nxt
