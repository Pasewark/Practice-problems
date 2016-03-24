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

def overlap(h1,h2):
    if h1==None or h2==None: return None
    l1=1
    l2=1
    current1=h1
    while current1.nxt!=None:
        l1+=1
        current1=current1.nxt
    current2=h2
    while current2.nxt!=None:
        l2+=1
        current2=current2.nxt
    if current1!=current2: return None
    current1=h1
    current2=h2
    if l1>l2:
        currentnum=l1-l2
        while currentnum>0:
            current1=current1.nxt
            currentnum-=1
    if l2>l1:
        currentnum=l2-l1
        while currentnum>0:
            current2=current2.nxt
            currentnum-=1
    while current1!=current2:
        current1=current1.nxt
        current2=current2.nxt
    return current1
