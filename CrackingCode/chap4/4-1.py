def dfs(g,n):
    visited,stack=set(),[n]
    while stack:
        current=stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(g[current]-visited)
    return visited

def route(g,n1,n2):
    if (n1 in dfs(g,n2)) or (n2 in dfs(g,n1)): return True
    return False
