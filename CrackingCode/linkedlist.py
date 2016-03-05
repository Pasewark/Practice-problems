#make a singly linked list class
class Node:
    nex=None
    def __init__(self,d):
        self.d=d
    def a(self,d):
        n=self
        while n.nex!=None:
            n=n.nex
        n.nex=Node(d)
    def p(self):
        n=self
        print n.d
        while n.nex!=None:
            n=n.nex
            print n.d

#remove node with given value
def remNode(head,d):
    h=head
    if h.d==d:
        return h.nex
    while h.nex!=None:
        if h.nex.d==d:
            h.nex=h.nex.nex
            return head
        h=h.nex
    return head

#remove duplicates
def remDup(head):
    s=set()
    current=head
    previous=None
    while current!=None:
        print current.d
        if current.d in s:
            previous.nex=current.nex
            current=previous
        s.add(current.d)
        previous=current
        current=current.nex
    return head
