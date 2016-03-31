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

d=[]
def balanced(b,n):
    if b.right!=None: balanced(b.right,n+1)
    if b.left!=None: balanced(b.left,n+1)
    if b.right==None or b.left==None: d.append(n)

def balance(b):
    balanced(b,0)
    m=min(d)
    M=max(d)
    if M-m>1: return False
    return True
