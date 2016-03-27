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

def delete(v):
    v.value=v.nxt.value
    v.nxt=v.nxt.nxt
