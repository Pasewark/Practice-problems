class stack:
    def __init__(self,n):
        self.elements=[0 for i in range(n)]
        self.index=0
    def pop(self):
        self.index-=1
        if self.index<0: return 'error'
        return self.elements[index]
    def push(self,value):
        if self.index==len(self.elements): return 'error'
        self.elements[self.index]=value
        self.index+=1

class SetOfStacks:
    def __init__(self,n):
        self.stacks=[]
        self.stacks.append(stack(n))
        self.n=n
    def addStack(self,value):
        s=stack(self.n)
        s.push(value)
        self.stacks.append(s)
    def pop():
        if self.stacks[-1].index>0: return self.stacks[-1].pop()
        else:
            if len(self.stacks)==1: return 'error'
            self.stacks.pop()
            return self.stacks[-1].pop()
    def push(value):
        if self.stacks[-1].index==n:
            self.addStack(value)
        else: self.stacks[-1].push(value)
