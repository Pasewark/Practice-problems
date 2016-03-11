class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def isPal(l):
    stack=[]
    current=l
    while current!=None:
        stack.append(current.value)
        current=current.nxt
    current=l
    while current!=None:
        if current.value!=stack.pop(): return False
        current=current.nxt
    return True

