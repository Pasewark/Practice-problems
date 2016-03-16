def sort(stack):
    temp=[]
    i=1
    while i<len(stack):
        for j in range(i):
            temp.append(stack.pop())
        current=stack.pop()
        appended=False
        while len(temp)>0:
            el=temp.pop()
            if current>el and not appended:
                stack.append(current)
                appended=True
            stack.append(el)
        if not appended: stack.append(current)
        i+=1
    return stack
