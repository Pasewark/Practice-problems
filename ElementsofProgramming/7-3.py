class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        print self.value
        current=self
        while current.nxt!=None:
            current=current.nxt
            print current.value

def cycle(L):
    current=L
    m=current
    st=set()
    st.add(current)
    while current.nxt!=None:
        current=current.nxt
        if current in st:break
        if current.value<m.value:
            m=current
    current=m
    nodes=set()
    nodes.add(current)
    currentm=current
    inc=0
    while current.nxt!=None:
        inc+=1
        inc%=2
        current=current.nxt
        if inc==0: currentm=currentm.nxt
        if current in nodes:
            if inc==0:
                return currentm.value
            else: return (currentm.value+currentm.nxt.value)/2
        nodes.add(current)
    return -1
