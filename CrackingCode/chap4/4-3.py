class node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value
    def prnt(self):
        if self.left!=None:
            self.left.prnt()
        print self.value
        if self.right!=None:
            self.right.prnt()

d={}
def lists(b,n):
    if n in d: d[n].append(b.value)
    else: d[n]=[b.value]
    if b.right!=None:
        lists(b.right,n+1)
    if b.left!=None:
        lists(b.left,n+1)
