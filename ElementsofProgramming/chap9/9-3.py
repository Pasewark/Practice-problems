class node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value

def helper(b1,b2):
    if b1==None and b2==None: return True
    if b1==None and b2!=None: return False
    if b2==None and b1!=None: return False
    if b1.value!=b2.value: return False
    if not helper(b1.left,b2.right): return False
    if not helper(b1.right,b2.left): return False
    return True

def symmetric(b):
    if b.right!=None and b.left!=None: return helper(b.right,b.left)
    else: return False
