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
def helper(b,l):
    if b.left!=None:
        helper(b.left,l)
    l.append(b.value)
    if b.right!=None:
        helper(b.right,l)
def isBin(b):
    l=[]
    helper(b,l)
    current=l[0]
    for i in l:
        if i<current: return False
        current=i
    return True
