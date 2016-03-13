def unique(s):
    characters=set()
    for c in s:
        if c in characters: return False
        characters.add(c)
    return True

def unique2(s):
    for i in xrange(len(s)-1):
        for j in xrange(i+1,len(s)):
            if s[i]==s[j]: return False
    return True
