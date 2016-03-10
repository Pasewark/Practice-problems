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

def merge(L,F):
    currentl=L
    currentf=F
    if currentl.value<currentf.value:
        head=currentl
        if currentl.nxt==None:
            head.nxt=currentf
            return head
        else:
            currentl=currentl.nxt
    else:
        head=currentf
        if currentf==None:
            head.nxt=currentl
            return head
        else:
            currentf=currentf.nxt
    current=head
    while True:
        if currentl.value<currentf.value:
            current.nxt=currentl
            if currentl.nxt==None:
                current.nxt.nxt=currentf
                return head
            else:
                currentl=currentl.nxt
        else:
            current.nxt=currentf
            if currentf==None:
                current.nxt.nxt=currentl
                return head
            else:
                currentf=currentf.nxt
        current=current.nxt

