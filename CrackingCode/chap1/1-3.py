def replaceSpace(s):
    l=s.split(" ")
    return "%20".join(l)

def replaceSpace2(s):
    output=''
    for char in s:
        if char==" ":
            output+="%20"
        else: output+=char
    return output
