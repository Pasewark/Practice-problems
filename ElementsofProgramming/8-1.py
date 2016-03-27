class maxstack:
    def __init__(self):
        self.elements=[]
    def pop(self):
        return self.elements.pop()[0]
    def push(self,element):
        if len(self.elements)==0:
            self.elements.append((element,element))
        else:
            self.elements.append((element,max(element,self.elements[-1][1])))
    def m(self):
        return self.elements[-1][1]
