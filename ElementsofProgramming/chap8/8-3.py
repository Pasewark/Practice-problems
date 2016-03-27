class node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value

def prnt(b):
    l=[]
    current=b
    while current!=None or len(l)>0:
        if current!=None:
            l.append(current)
            current=current.left
        else:
            current=l.pop()
            print current.value
            current=current.right
        
