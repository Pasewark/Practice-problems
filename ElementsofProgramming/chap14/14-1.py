class node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value

def isbin(b):
    if b==None: return True
    if b.right!=None and b.right.value<b.value:
        return False
    if b.left!=None and b.left.value>b.value:
        return False
    if not isbin(b.right): return False
    if not isbin(b.left): return False
    return True
