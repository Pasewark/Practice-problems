def isPerm(s):
    d={}
    for char in s:
        if char in d: d[char]+=1
        else: d[char]=1
    if len(s)%2==0:
        for key in d:
            if d[key]%2!=0: return False
        return True
    else:
        odd=0
        for key in d:
            if d[key]%2!=0:
                if odd==0: odd+=1
                else: return False
        return True
