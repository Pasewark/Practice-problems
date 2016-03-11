class node:
    nxt=None
    def __init__(self,value):
        self.value=value
    def prnt(self):
        current=self
        while current!=None:
            print current.value
            current=current.nxt

def part(l,v):
    firstlower=None
    firstgreater=None
    lower=None
    greater=None
    current=l
    while current!=None:
        if current.value<v:
            if firstlower==None:
                firstlower=current
                lower=current
            else:
                lower.nxt=current
                lower=lower.nxt
            current=current.nxt
            lower.nxt=None
        else:
            if firstgreater==None:
                firstgreater=current
                greater=current
            else:
                greater.nxt=current
                greater=greater.nxt
            current=current.nxt
            greater.nxt=None
    lower.nxt=firstgreater
    return firstlower
