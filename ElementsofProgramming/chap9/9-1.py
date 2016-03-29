class node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value

def balanced(b):
    maxh=0
    minh=-1
    l=[]
    current=b
    currenth=0
    while current!=None or len(l)>0:
        if current!=None:
            l.append(current)
            current=current.left
            currenth+=1
        else:
            current=l.pop()
            currenth-=1
            if current.right==None and current.left==None:
                maxh=max(maxh,currenth)
                if minh==-1: minh=currenth
                else: minh=min(minh,currenth)
            current=current.right
    return maxh-minh<2
