class minStack:
    def __init__(self):
        self.elements=[]
        self.minimums=[]
    def push(self,value):
        self.elements.append(value)
        if len(self.minimums)==0: self.minimums.append(value)
        else: self.minimums.append(min(value,self.minimums[-1]))
    def pop(self):
        if len(self.elements)==0: return 'error'
        self.minimums.pop()
        return self.elements.pop()
    def minimum(self):
        if len(self.elements)==0: return 'error'
        return self.minimums[-1]
