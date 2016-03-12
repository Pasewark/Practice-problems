class queue:
    stack1=[]
    stack2=[]
    def __init__(self):
        return
    def enqueue(self,value):
        self.stack1.append(value)
    def dequeue(self):
        while len(self.stack1)>1:
            self.stack2.append(self.stack1.pop())
        a=self.stack1.pop()
        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())
        return a
    def isEmpty(self):
        return len(self.stack1)==0
