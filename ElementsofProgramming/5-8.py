def decode(s):
    n=0
    for c in s:
        n*=26
        n+=ord(c)-64
    return n
