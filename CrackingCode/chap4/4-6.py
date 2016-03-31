class node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value
        self.p=None
    def prnt(self):
        if self.left!=None:
            self.left.prnt()
        print self.value
        if self.right!=None:
            self.right.prnt()
            
def succ(b,n):
    if n.right!=None:
        current=n.right
        while current.left!=None:
            current=current.left
        return current.value
    current=n
    while True:
        if current.p==None: return -1
        if current.p.left==current: return current.p.value
        current=current.p
        
    return current.value
