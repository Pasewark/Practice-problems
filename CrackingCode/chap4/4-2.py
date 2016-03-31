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

def mktree(l):
    if len(l)==1:
        return node(l[0])
    if len(l)==2:
        a=node(l[0])
        a.right=node(l[1])
        return a
    mid=len(l)/2
    rt=node(l[mid])
    rt.left=mktree(l[:mid])
    rt.right=mktree(l[mid+1:])
    return rt
