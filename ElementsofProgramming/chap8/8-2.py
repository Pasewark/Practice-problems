def evaluate(e):
    stack=[]
    for i in e:
        if type(i) is int:
            stack.append(i)
        else:
            if i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='-':
                a=stack.pop()
                stack.append(stack.pop()-a)
            elif i=='*':
                stack.append(stack.pop()*stack.pop())
            else:
                a=stack.pop()
                stack.append(stack.pop()/a)
    return stack.pop()
